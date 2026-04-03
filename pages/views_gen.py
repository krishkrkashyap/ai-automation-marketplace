# views.py - auto-generated
from django.shortcuts import render

INDUSTRIES = [
    {'name': 'E-Commerce', 'icon': 'E-Commerce', 'url': '/industries/ecommerce-automation/'},
    {'name': 'Finance', 'icon': 'Finance', 'url': '/industries/finance-automation/'},
    {'name': 'Healthcare', 'icon': 'Healthcare', 'url': '/industries/healthcare-automation/'},
    {'name': 'Education', 'icon': 'Education', 'url': '/industries/education-automation/'},
    {'name': 'Real Estate', 'icon': 'Real Estate', 'url': '/industries/real-estate-automation/'},
    {'name': 'Marketing', 'icon': 'Marketing', 'url': '/industries/marketing-automation/'},
    {'name': 'HR', 'icon': 'HR', 'url': '/industries/hr-automation/'},
    {'name': 'Legal', 'icon': 'Legal', 'url': '/industries/legal-automation/'},
    {'name': 'Manufacturing', 'icon': 'Manufacturing', 'url': '/industries/manufacturing-automation/'},
    {'name': 'Logistics', 'icon': 'Logistics', 'url': '/industries/logistics-automation/'},
    {'name': 'Banking', 'icon': 'Banking', 'url': '/industries/banking-fintech-automation/'},
    {'name': 'Energy', 'icon': 'Energy', 'url': '/industries/energy-utilities-automation/'},
    {'name': 'Travel', 'icon': 'Travel', 'url': '/industries/travel-automation/'},
    {'name': 'Media', 'icon': 'Media', 'url': '/industries/media-creative-automation/'},
    {'name': 'Government', 'icon': 'Government', 'url': '/industries/government-automation/'},
    {'name': 'Agriculture', 'icon': 'Agriculture', 'url': '/industries/agriculture-automation/'},
    {'name': 'Security', 'icon': 'Security', 'url': '/industries/security-automation/'},
    {'name': 'Automotive', 'icon': 'Automotive', 'url': '/industries/automotive-automation/'},
]

SERVICES = [
    {'name': 'AI Chatbots', 'description': 'Intelligent conversational agents', 'icon': 'fas fa-comments', 'url': '/services/ai-chatbots/'},
    {'name': 'RPA Solutions', 'description': 'Robotic process automation', 'icon': 'fas fa-robot', 'url': '/services/rpa/'},
    {'name': 'Sales Automation', 'description': 'Automate sales pipeline', 'icon': 'fas fa-chart-line', 'url': '/services/sales-automation/'},
    {'name': 'Marketing Automation', 'description': 'Streamline marketing campaigns', 'icon': 'fas fa-bullhorn', 'url': '/services/marketing-automation/'},
    {'name': 'Finance Automation', 'description': 'Automate invoicing', 'icon': 'fas fa-file-invoice-dollar', 'url': '/services/finance-automation/'},
    {'name': 'Data Automation', 'description': 'ETL and data processing', 'icon': 'fas fa-database', 'url': '/services/data-automation/'},
]

BOTS = [
    {'name': 'Lead Qualification Bot', 'description': 'Auto-qualify leads 24/7', 'icon': 'robot', 'url': '/services/bots/lead-qualification-bot/'},
    {'name': 'Invoice Processing', 'description': 'Automated invoice extraction', 'icon': 'file', 'url': '/services/bots/invoice-processing-bot/'},
    {'name': 'Customer Support', 'description': 'AI-powered support bot', 'icon': 'comment', 'url': '/services/bots/customer-support-bot/'},
    {'name': 'Fraud Detection', 'description': 'Real-time fraud prevention', 'icon': 'shield', 'url': '/services/bots/fraud-detection-bot/'},
]

def home(request):
    return render(request, 'pages/home.html', {'industries': INDUSTRIES, 'services': SERVICES, 'bots': BOTS})

def industries_list(request):
    return render(request, 'pages/industries_list.html', {'industries': INDUSTRIES})

def industry_detail(request, industry_slug):
    industry_data = {
        'ecommerce-automation': {'name': 'E-Commerce Automation', 'icon': 'E-Commerce', 'description': 'Transform your online store with AI-powered automation.', 'problems': ['Manual inventory tracking errors', 'Slow customer response times', 'Complex order processing'], 'solutions': ['AI-powered inventory prediction', 'Intelligent chatbots', 'Automated order processing']},
        'finance-automation': {'name': 'Finance and Banking Automation', 'icon': 'Finance', 'description': 'Revolutionize financial operations with intelligent automation.', 'problems': ['Manual invoice processing', 'Complex reconciliation', 'Slow reporting'], 'solutions': ['Invoice OCR automation', 'Automated reconciliation', 'Real-time dashboards']},
        'healthcare-automation': {'name': 'Healthcare Automation', 'icon': 'Healthcare', 'description': 'Streamline healthcare operations with AI automation.', 'problems': ['Administrative overhead', 'Appointment scheduling', 'Medical transcription errors'], 'solutions': ['Smart scheduling', 'AI transcription', 'EMR automation']},
    }
    industry = industry_data.get(industry_slug, {'name': industry_slug.replace('-', ' ').title(), 'icon': 'AI', 'description': 'AI automation solutions', 'problems': ['Manual processes'], 'solutions': ['Automation solutions']})
    return render(request, 'pages/industry_detail.html', {'industry': industry, 'slug': industry_slug})

def services_list(request):
    return render(request, 'pages/services_list.html', {'services': SERVICES})

def service_detail(request, service_slug):
    return render(request, 'pages/service_detail.html', {'slug': service_slug})

def bot_detail(request, bot_slug):
    bots_data = {
        'lead-qualification-bot': {'name': 'Lead Qualification Bot', 'industry': 'Sales and Marketing', 'description': 'Automatically qualify leads 24/7.', 'features': ['Automated lead scoring', 'Custom qualification questions', 'CRM integration'], 'use_cases': ['E-Commerce', 'SaaS', 'Real Estate']},
        'invoice-processing-bot': {'name': 'Invoice Processing Bot', 'industry': 'Finance and Accounting', 'description': 'Automate invoice extraction with AI-powered OCR.', 'features': ['OCR extraction', 'Automatic validation', 'Approval workflow'], 'use_cases': ['Finance', 'Healthcare', 'Manufacturing']},
    }
    bot = bots_data.get(bot_slug, {'name': bot_slug.replace('-', ' ').title(), 'industry': 'General', 'description': 'AI bot', 'features': ['Feature 1'], 'use_cases': ['All Industries']})
    return render(request, 'pages/bot_detail.html', {'bot': bot, 'slug': bot_slug})

def case_studies(request):
    return render(request, 'pages/case_studies.html')

def pricing(request):
    pricing_tiers = [
        {'name': 'Starter', 'price': '499', 'description': 'Perfect for small businesses', 'features': ['1 AI Bot', 'Basic integration', 'Email support']},
        {'name': 'Professional', 'price': '1499', 'description': 'For growing businesses', 'features': ['3 AI Bots', 'Advanced integrations', 'Priority support']},
        {'name': 'Enterprise', 'price': 'Custom', 'description': 'For large organizations', 'features': ['Unlimited bots', 'Full integrations', '24/7 support']},
    ]
    return render(request, 'pages/pricing.html', {'pricing_tiers': pricing_tiers})

def contact(request):
    return render(request, 'pages/contact.html')
