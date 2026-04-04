import os
import json
import requests
from datetime import datetime
from typing import Dict, List, Optional, Any
from django.conf import settings

N8N_API_URL = os.environ.get('N8N_API_URL', 'https://krishkrkashya.app.n8n.cloud')
N8N_API_KEY = os.environ.get('N8N_API_KEY', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI4MTk5ZWIxNS0wYTNkLTQyNWUtOWQ0Zi0yZmY0OWYyMTgwYjQiLCJpc3MiOiJuOG4iLCJhdWQiOiJtY3Atc2VydmVyLWFwaSIsImp0aSI6IjU0NjVmZGEzLTY4YjYtNGY1NC1hZWMzLTM2ODUyMDQzYjQzOCIsImlhdCI6MTc3NTI0MDc5Mn0.vWh1XauyD1nNMRrXAM08-SsIASaNiXh1PQ0b8Rl8ffE')

HEADERS = {
    'Authorization': f'Bearer {N8N_API_KEY}',
    'Content-Type': 'application/json'
}

WORKFLOW_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'n8n-workflows')


class N8NWorkflowManager:
    def __init__(self):
        self.api_url = N8N_API_URL
        self.api_key = N8N_API_KEY
        self.headers = HEADERS
    
    def get_workflows(self) -> List[Dict]:
        try:
            response = requests.get(f'{self.api_url}/api/workflows', headers=self.headers, timeout=30)
            if response.status_code == 200:
                return response.json().get('data', [])
            return []
        except Exception as e:
            print(f"Error fetching workflows: {e}")
            return []
    
    def get_workflow(self, workflow_id: str) -> Optional[Dict]:
        try:
            response = requests.get(f'{self.api_url}/api/workflows/{workflow_id}', headers=self.headers, timeout=30)
            if response.status_code == 200:
                return response.json()
            return None
        except Exception as e:
            print(f"Error fetching workflow: {e}")
            return None
    
    def create_workflow(self, name: str, nodes: List[Dict], connections: Dict) -> Optional[Dict]:
        workflow_data = {
            'name': name,
            'nodes': nodes,
            'connections': connections,
            'active': False,
            'settings': {'executionOrder': 'v1'}
        }
        try:
            response = requests.post(
                f'{self.api_url}/api/workflows',
                headers=self.headers,
                json=workflow_data,
                timeout=30
            )
            if response.status_code in [200, 201]:
                return response.json()
            return None
        except Exception as e:
            print(f"Error creating workflow: {e}")
            return None
    
    def activate_workflow(self, workflow_id: str) -> bool:
        try:
            response = requests.post(
                f'{self.api_url}/api/workflows/{workflow_id}/activate',
                headers=self.headers,
                timeout=30
            )
            return response.status_code in [200, 201]
        except Exception as e:
            print(f"Error activating workflow: {e}")
            return False
    
    def deactivate_workflow(self, workflow_id: str) -> bool:
        try:
            response = requests.post(
                f'{self.api_url}/api/workflows/{workflow_id}/deactivate',
                headers=self.headers,
                timeout=30
            )
            return response.status_code in [200, 201]
        except Exception as e:
            print(f"Error deactivating workflow: {e}")
            return False
    
    def execute_workflow(self, workflow_id: str, data: Dict) -> Optional[Dict]:
        try:
            response = requests.post(
                f'{self.api_url}/api/webhook/{workflow_id}',
                json=data,
                headers={'Content-Type': 'application/json'},
                timeout=60
            )
            if response.status_code in [200, 201, 202]:
                try:
                    return response.json()
                except:
                    return {'result': response.text}
            return None
        except Exception as e:
            print(f"Error executing workflow: {e}")
            return None
    
    def get_executions(self, workflow_id: Optional[str] = None, limit: int = 10) -> List[Dict]:
        try:
            url = f'{self.api_url}/api/executions'
            params = {'limit': limit}
            if workflow_id:
                params['workflowId'] = workflow_id
            response = requests.get(url, headers=self.headers, params=params, timeout=30)
            if response.status_code == 200:
                return response.json().get('data', [])
            return []
        except Exception as e:
            print(f"Error fetching executions: {e}")
            return []
    
    def load_workflow_template(self, slug: str) -> Optional[Dict]:
        template_path = os.path.join(WORKFLOW_DIR, f'{slug}.json')
        try:
            with open(template_path, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading template: {e}")
            return None
    
    def create_workflow_from_template(self, template_slug: str, name: str) -> Optional[Dict]:
        template = self.load_workflow_template(template_slug)
        if not template:
            return None
        template['name'] = name
        return self.create_workflow(name, template.get('nodes', []), template.get('connections', {}))


workflow_manager = N8NWorkflowManager()


AUTOMATION_WORKFLOWS = {
    'business-process-automation': {
        'name': 'Business Process Automation',
        'description': 'Streamline workflows and automate approvals',
        'trigger': 'Webhook',
        'n8n_path': 'business-process-automation',
        'api_endpoint': '/api/business-process',
    },
    'robotic-process-automation': {
        'name': 'Robotic Process Automation',
        'description': 'Automate repetitive tasks and legacy system interactions',
        'trigger': 'Schedule',
        'n8n_path': 'rpa-automation',
        'api_endpoint': '/api/rpa',
    },
    'ai-chatbot-automation': {
        'name': 'AI Chatbot & Conversational Automation',
        'description': 'Build intelligent conversational agents',
        'trigger': 'Webhook',
        'n8n_path': 'ai-chatbot-automation',
        'api_endpoint': '/api/chatbot',
    },
    'sales-automation': {
        'name': 'Sales Automation',
        'description': 'Automate sales pipeline from lead to deal',
        'trigger': 'Webhook',
        'n8n_path': 'sales-automation',
        'api_endpoint': '/api/sales',
    },
    'marketing-automation': {
        'name': 'Marketing Automation',
        'description': 'Create and optimize marketing campaigns',
        'trigger': 'Schedule',
        'n8n_path': 'marketing-automation',
        'api_endpoint': '/api/marketing',
    },
    'customer-support-automation': {
        'name': 'Customer Support Automation',
        'description': 'Transform customer service with AI',
        'trigger': 'Webhook',
        'n8n_path': 'customer-support-automation',
        'api_endpoint': '/api/support',
    },
    'finance-automation': {
        'name': 'Finance & Accounting Automation',
        'description': 'Automate invoicing and financial processes',
        'trigger': 'Webhook',
        'n8n_path': 'finance-automation',
        'api_endpoint': '/api/finance',
    },
    'hr-automation': {
        'name': 'HR & Workforce Automation',
        'description': 'Streamline recruitment and HR processes',
        'trigger': 'Webhook',
        'n8n_path': 'hr-automation',
        'api_endpoint': '/api/hr',
    },
    'it-devops-automation': {
        'name': 'IT & DevOps Automation',
        'description': 'Automate CI/CD and infrastructure',
        'trigger': 'Git Webhook',
        'n8n_path': 'devops-automation',
        'api_endpoint': '/api/devops',
    },
    'data-automation': {
        'name': 'Data Automation & Intelligence',
        'description': 'ETL pipelines and data processing',
        'trigger': 'Schedule',
        'n8n_path': 'data-automation',
        'api_endpoint': '/api/data',
    },
    'ai-ml-automation': {
        'name': 'AI & Machine Learning Automation',
        'description': 'Deploy and manage ML models',
        'trigger': 'Webhook',
        'n8n_path': 'ai-ml-automation',
        'api_endpoint': '/api/ai-ml',
    },
    'document-automation': {
        'name': 'Document & Content Automation',
        'description': 'Generate and process documents',
        'trigger': 'Webhook',
        'n8n_path': 'document-automation',
        'api_endpoint': '/api/document',
    },
    'ecommerce-automation': {
        'name': 'E-commerce Automation',
        'description': 'Automate online store operations',
        'trigger': 'Webhook',
        'n8n_path': 'ecommerce-automation',
        'api_endpoint': '/api/ecommerce',
    },
    'manufacturing-automation': {
        'name': 'Manufacturing & Industrial Automation',
        'description': 'IoT monitoring and predictive maintenance',
        'trigger': 'Schedule',
        'n8n_path': 'manufacturing-automation',
        'api_endpoint': '/api/manufacturing',
    },
    'logistics-automation': {
        'name': 'Logistics & Supply Chain Automation',
        'description': 'Route optimization and tracking',
        'trigger': 'Webhook',
        'n8n_path': 'logistics-automation',
        'api_endpoint': '/api/logistics',
    },
    'healthcare-automation': {
        'name': 'Healthcare Automation',
        'description': 'Patient scheduling and medical workflows',
        'trigger': 'Webhook',
        'n8n_path': 'healthcare-automation',
        'api_endpoint': '/api/healthcare',
    },
    'banking-automation': {
        'name': 'Banking & Fintech Automation',
        'description': 'KYC, fraud detection, and compliance',
        'trigger': 'Webhook',
        'n8n_path': 'banking-automation',
        'api_endpoint': '/api/banking',
    },
    'legal-automation': {
        'name': 'Legal & Compliance Automation',
        'description': 'Contract lifecycle and compliance',
        'trigger': 'Webhook',
        'n8n_path': 'legal-automation',
        'api_endpoint': '/api/legal',
    },
    'education-automation': {
        'name': 'Education & EdTech Automation',
        'description': 'AI tutoring and grading',
        'trigger': 'Webhook',
        'n8n_path': 'education-automation',
        'api_endpoint': '/api/education',
    },
    'real-estate-automation': {
        'name': 'Real Estate Automation',
        'description': 'Property listings and lead management',
        'trigger': 'Webhook',
        'n8n_path': 'real-estate-automation',
        'api_endpoint': '/api/real-estate',
    },
    'media-automation': {
        'name': 'Media & Creative Automation',
        'description': 'Content creation and publishing',
        'trigger': 'Schedule',
        'n8n_path': 'media-automation',
        'api_endpoint': '/api/media',
    },
    'government-automation': {
        'name': 'Government & Public Sector Automation',
        'description': 'Citizen services and permits',
        'trigger': 'Webhook',
        'n8n_path': 'government-automation',
        'api_endpoint': '/api/government',
    },
    'energy-automation': {
        'name': 'Energy, Utilities & Environment Automation',
        'description': 'Grid optimization and monitoring',
        'trigger': 'Schedule',
        'n8n_path': 'energy-automation',
        'api_endpoint': '/api/energy',
    },
    'agriculture-automation': {
        'name': 'Agriculture & AgriTech Automation',
        'description': 'Crop monitoring and farming automation',
        'trigger': 'Schedule',
        'n8n_path': 'agriculture-automation',
        'api_endpoint': '/api/agriculture',
    },
    'security-fraud-automation': {
        'name': 'Security, Risk & Fraud Automation',
        'description': 'Threat detection and access control',
        'trigger': 'Schedule',
        'n8n_path': 'security-automation',
        'api_endpoint': '/api/security',
    },
    'nocode-lowcode-automation': {
        'name': 'No-Code / Low-Code Automation Services',
        'description': 'Zapier, Make, Power Automate workflows',
        'trigger': 'Webhook',
        'n8n_path': 'nocode-automation',
        'api_endpoint': '/api/nocode',
    },
    'fullcode-custom-automation': {
        'name': 'Full-Code / Custom Automation Services',
        'description': 'Custom AI agents and integrations',
        'trigger': 'Webhook',
        'n8n_path': 'fullcode-automation',
        'api_endpoint': '/api/fullcode',
    },
    'ai-strategy-consulting': {
        'name': 'AI Strategy & Automation Consulting',
        'description': 'Strategy and implementation planning',
        'trigger': 'Webhook',
        'n8n_path': 'consulting-automation',
        'api_endpoint': '/api/consulting',
    },
}
