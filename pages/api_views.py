from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from pages.n8n_integration import workflow_manager, AUTOMATION_WORKFLOWS

@require_http_methods(["GET"])
def workflow_status(request, automation_slug):
    workflow_info = AUTOMATION_WORKFLOWS.get(automation_slug)
    if not workflow_info:
        return JsonResponse({'error': 'Automation not found'}, status=404)
    
    n8n_path = workflow_info.get('n8n_path', automation_slug)
    template = workflow_manager.load_workflow_template(n8n_path)
    
    return JsonResponse({
        'automation_slug': automation_slug,
        'name': workflow_info['name'],
        'description': workflow_info['description'],
        'trigger': workflow_info['trigger'],
        'api_endpoint': workflow_info['api_endpoint'],
        'template_exists': template is not None,
        'workflow': template.get('name') if template else None,
    })

@require_http_methods(["GET"])
def list_workflows(request):
    workflows = []
    for slug, info in AUTOMATION_WORKFLOWS.items():
        template = workflow_manager.load_workflow_template(info['n8n_path'])
        workflows.append({
            'slug': slug,
            'name': info['name'],
            'description': info['description'],
            'trigger': info['trigger'],
            'api_endpoint': info['api_endpoint'],
            'template_available': template is not None
        })
    return JsonResponse({'workflows': workflows, 'count': len(workflows)})

@csrf_exempt
@require_http_methods(["POST"])
def execute_workflow(request, automation_slug):
    workflow_info = AUTOMATION_WORKFLOWS.get(automation_slug)
    if not workflow_info:
        return JsonResponse({'error': 'Automation not found'}, status=404)
    
    try:
        data = json.loads(request.body) if request.body else {}
    except:
        data = {}
    
    n8n_path = workflow_info.get('n8n_path', automation_slug)
    result = workflow_manager.execute_workflow(n8n_path, data)
    
    if result:
        return JsonResponse({
            'status': 'success',
            'message': f"Workflow '{workflow_info['name']}' executed",
            'result': result
        })
    else:
        return JsonResponse({
            'status': 'pending',
            'message': 'Workflow triggered, awaiting response'
        })

@csrf_exempt
@require_http_methods(["POST"])
def create_workflow(request, automation_slug):
    workflow_info = AUTOMATION_WORKFLOWS.get(automation_slug)
    if not workflow_info:
        return JsonResponse({'error': 'Automation not found'}, status=404)
    
    try:
        data = json.loads(request.body) if request.body else {}
        name = data.get('name', f"{workflow_info['name']} - {automation_slug}")
    except:
        name = f"{workflow_info['name']} - {automation_slug}"
    
    result = workflow_manager.create_workflow_from_template(
        workflow_info['n8n_path'],
        name
    )
    
    if result:
        return JsonResponse({
            'status': 'success',
            'message': 'Workflow created',
            'workflow_id': result.get('id'),
            'workflow_name': result.get('name')
        })
    else:
        return JsonResponse({
            'status': 'error',
            'message': 'Failed to create workflow from template'
        }, status=500)

@require_http_methods(["GET"])
def workflow_executions(request, automation_slug):
    workflow_info = AUTOMATION_WORKFLOWS.get(automation_slug)
    if not workflow_info:
        return JsonResponse({'error': 'Automation not found'}, status=404)
    
    limit = int(request.GET.get('limit', 10))
    executions = workflow_manager.get_executions(limit=limit)
    
    return JsonResponse({
        'automation': workflow_info['name'],
        'executions': executions[:limit],
        'count': len(executions)
    })

@require_http_methods(["GET"])
def api_root(request):
    return JsonResponse({
        'service': 'AI Automation Marketplace API',
        'version': '1.0.0',
        'endpoints': {
            'list_workflows': '/api/workflows/',
            'workflow_status': '/api/workflows/<slug>/status/',
            'execute_workflow': '/api/workflows/<slug>/execute/',
            'create_workflow': '/api/workflows/<slug>/create/',
            'workflow_executions': '/api/workflows/<slug>/executions/',
            'automation_api': '/api/automations/<service>/',
        }
    })
