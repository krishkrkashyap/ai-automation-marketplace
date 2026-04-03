from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.views.generic import RedirectView

INDUSTRIES = [
    {'name': 'E-Commerce', 'slug': 'ecommerce-automation', 'url': '/industries/ecommerce-automation/'},
    {'name': 'Finance', 'slug': 'finance-automation', 'url': '/industries/finance-automation/'},
    {'name': 'Healthcare', 'slug': 'healthcare-automation', 'url': '/industries/healthcare-automation/'},
    {'name': 'Education', 'slug': 'education-automation', 'url': '/industries/education-automation/'},
    {'name': 'Real Estate', 'slug': 'real-estate-automation', 'url': '/industries/real-estate-automation/'},
    {'name': 'Marketing', 'slug': 'marketing-automation', 'url': '/industries/marketing-automation/'},
    {'name': 'HR', 'slug': 'hr-automation', 'url': '/industries/hr-automation/'},
    {'name': 'Legal', 'slug': 'legal-automation', 'url': '/industries/legal-automation/'},
    {'name': 'Manufacturing', 'slug': 'manufacturing-automation', 'url': '/industries/manufacturing-automation/'},
    {'name': 'Logistics', 'slug': 'logistics-supply-chain-automation', 'url': '/industries/logistics-supply-chain-automation/'},
    {'name': 'Banking', 'slug': 'banking-fintech-automation', 'url': '/industries/banking-fintech-automation/'},
    {'name': 'Energy', 'slug': 'energy-utilities-automation', 'url': '/industries/energy-utilities-automation/'},
    {'name': 'Travel', 'slug': 'travel-automation', 'url': '/industries/travel-automation/'},
    {'name': 'Media', 'slug': 'media-creative-automation', 'url': '/industries/media-creative-automation/'},
    {'name': 'Government', 'slug': 'government-automation', 'url': '/industries/government-automation/'},
    {'name': 'Agriculture', 'slug': 'agriculture-automation', 'url': '/industries/agriculture-automation/'},
    {'name': 'Security', 'slug': 'security-automation', 'url': '/industries/security-automation/'},
    {'name': 'Automotive', 'slug': 'automotive-automation', 'url': '/industries/automotive-automation/'},
]

SERVICES = [
    {'name': 'AI Chatbots', 'description': 'Intelligent conversational agents', 'icon': 'fas fa-comments', 'url': '/services/ai-chatbots/'},
    {'name': 'RPA Solutions', 'description': 'Robotic process automation', 'icon': 'fas fa-robot', 'url': '/services/rpa/'},
    {'name': 'Sales Automation', 'description': 'Automate sales pipeline', 'icon': 'fas fa-chart-line', 'url': '/services/sales-automation/'},
    {'name': 'Marketing Automation', 'description': 'Streamline marketing campaigns', 'icon': 'fas fa-bullhorn', 'url': '/services/marketing-automation/'},
    {'name': 'Finance Automation', 'description': 'Automate invoicing', 'icon': 'fas fa-file-invoice-dollar', 'url': '/services/finance-automation/'},
    {'name': 'Data Automation', 'description': 'ETL and data processing', 'icon': 'fas fa-database', 'url': '/services/data-automation/'},
    {'name': 'Customer Support', 'description': 'AI support automation', 'icon': 'fas fa-headset', 'url': '/services/customer-support-automation/'},
    {'name': 'HR Automation', 'description': 'Workforce management', 'icon': 'fas fa-users', 'url': '/services/hr-automation/'},
    {'name': 'IT DevOps', 'description': 'Infrastructure automation', 'icon': 'fas fa-server', 'url': '/services/it-devops-automation/'},
    {'name': 'Document Automation', 'description': 'Document processing', 'icon': 'fas fa-file-alt', 'url': '/services/document-automation/'},
]

BOTS = [
    {'name': 'Lead Qualification Bot', 'slug': 'lead-qualification-bot', 'description': 'Auto-qualify leads 24/7', 'url': '/services/bots/lead-qualification-bot/'},
    {'name': 'Invoice Processing', 'slug': 'invoice-processing-bot', 'description': 'Automated invoice extraction', 'url': '/services/bots/invoice-processing-bot/'},
    {'name': 'Customer Support', 'slug': 'customer-support-bot', 'description': 'AI-powered support bot', 'url': '/services/bots/customer-support-bot/'},
    {'name': 'Fraud Detection', 'slug': 'fraud-detection-bot', 'description': 'Real-time fraud prevention', 'url': '/services/bots/fraud-detection-bot/'},
    {'name': 'Product Scraping', 'slug': 'product-scraping-bot', 'description': 'E-commerce data extraction', 'url': '/services/bots/product-scraping-bot/'},
    {'name': 'Inventory Prediction', 'slug': 'inventory-prediction-bot', 'description': 'AI demand forecasting', 'url': '/services/bots/inventory-prediction-bot/'},
    {'name': 'Resume Screening', 'slug': 'resume-screening-bot', 'description': 'Automated candidate review', 'url': '/services/bots/resume-screening-bot/'},
    {'name': 'Meeting Booking', 'slug': 'meeting-booking-bot', 'description': 'Scheduling automation', 'url': '/services/bots/meeting-booking-bot/'},
    {'name': 'Social Media', 'slug': 'social-media-bot', 'description': 'Content automation', 'url': '/services/bots/social-media-bot/'},
    {'name': 'Email Automation', 'slug': 'email-automation-bot', 'description': 'Email campaign management', 'url': '/services/bots/email-automation-bot/'},
    {'name': 'Data Entry', 'slug': 'data-entry-bot', 'description': 'Automated data input', 'url': '/services/bots/data-entry-bot/'},
    {'name': 'Expense Processing', 'slug': 'expense-processing-bot', 'description': 'Receipt automation', 'url': '/services/bots/expense-processing-bot/'},
    {'name': 'KYC Verification', 'slug': 'kyc-verification-bot', 'description': 'Identity verification', 'url': '/services/bots/kyc-verification-bot/'},
    {'name': 'Claim Processing', 'slug': 'claim-processing-bot', 'description': 'Insurance claims automation', 'url': '/services/bots/claim-processing-bot/'},
    {'name': 'Patient Triage', 'slug': 'patient-triage-bot', 'description': 'Medical triage AI', 'url': '/services/bots/patient-triage-bot/'},
    {'name': 'Compliance Monitoring', 'slug': 'compliance-monitoring-bot', 'description': 'Regulatory automation', 'url': '/services/bots/compliance-monitoring-bot/'},
]

INDUSTRY_DATA = {
    'ecommerce-automation': {'name': 'E-Commerce Automation', 'icon': 'E-Commerce', 'description': 'Transform your online store with AI-powered automation. From inventory management to customer support.', 'problems': ['Manual inventory tracking', 'Slow response times', 'Order processing'], 'solutions': ['AI inventory prediction', 'Intelligent chatbots', 'Automated order processing']},
    'finance-automation': {'name': 'Finance and Banking Automation', 'icon': 'Finance', 'description': 'Revolutionize financial operations with intelligent automation.', 'problems': ['Manual invoice processing', 'Complex reconciliation', 'Slow reporting'], 'solutions': ['Invoice OCR automation', 'Automated reconciliation', 'Real-time dashboards']},
    'healthcare-automation': {'name': 'Healthcare Automation', 'icon': 'Healthcare', 'description': 'Streamline healthcare operations with AI automation.', 'problems': ['Administrative overhead', 'Scheduling chaos', 'Transcription errors'], 'solutions': ['Smart scheduling', 'AI transcription', 'EMR automation']},
}

BOTS_DATA = {
    'lead-qualification-bot': {'name': 'Lead Qualification Bot', 'industry': 'Sales and Marketing', 'description': 'Automatically qualify leads 24/7 with AI-powered bots.', 'features': ['Automated lead scoring', 'CRM integration', 'Real-time notifications'], 'use_cases': ['E-Commerce', 'SaaS', 'Real Estate']},
    'invoice-processing-bot': {'name': 'Invoice Processing Bot', 'industry': 'Finance', 'description': 'Automate invoice extraction with AI-powered OCR.', 'features': ['OCR extraction', 'Validation', 'Approval workflow'], 'use_cases': ['Finance', 'Healthcare']},
    'customer-support-bot': {'name': 'Customer Support Bot', 'industry': 'Customer Service', 'description': 'AI-powered chatbot for 24/7 support.', 'features': ['NLP', 'Multi-language', 'Knowledge base'], 'use_cases': ['E-Commerce', 'SaaS']},
    'fraud-detection-bot': {'name': 'Fraud Detection Bot', 'industry': 'Security', 'description': 'Real-time fraud detection using AI.', 'features': ['Transaction monitoring', 'Pattern recognition', 'Risk scoring'], 'use_cases': ['Banking', 'E-Commerce']},
}

def home(request):
    return render(request, 'pages/home.html', {'industries': INDUSTRIES, 'services': SERVICES, 'bots': BOTS})

def industries_list(request):
    return render(request, 'pages/industries_list.html', {'industries': INDUSTRIES})

def industry_detail(request, industry_slug):
    if industry_slug not in INDUSTRY_DATA:
        industry = {'name': industry_slug.replace('-', ' ').title(), 'icon': 'AI', 'description': 'AI automation solutions', 'problems': ['Manual processes'], 'solutions': ['Automation']}
    else:
        industry = INDUSTRY_DATA[industry_slug]
    return render(request, 'pages/industry_detail.html', {'industry': industry, 'slug': industry_slug})

def services_list(request):
    return render(request, 'pages/services_list.html', {'services': SERVICES})

def service_detail(request, service_slug):
    return render(request, 'pages/service_detail.html', {'slug': service_slug})

def bot_detail(request, bot_slug):
    if bot_slug not in BOTS_DATA:
        bot = {'name': bot_slug.replace('-', ' ').title(), 'industry': 'General', 'description': 'AI bot', 'features': ['Feature'], 'use_cases': ['All']}
    else:
        bot = BOTS_DATA[bot_slug]
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

def sitemap_xml(request):
    sites = []
    for ind in INDUSTRIES:
        sites.append(f"https://example.com/industries/{ind['slug']}/")
    for bot in BOTS:
        sites.append(f"https://example.com/services/bots/{bot['slug']}/")
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    xml += '<url><loc>https://example.com/</loc><priority>1.0</priority></url>\n'
    for site in sites:
        xml += f'<url><loc>{site}</loc><priority>0.8</priority></url>\n'
    xml += '</urlset>'
    return HttpResponse(xml, content_type='application/xml')

def robots_txt(request):
    txt = "User-agent: *\nAllow: /\nSitemap: https://example.com/sitemap.xml\n"
    return HttpResponse(txt, content_type='text/plain')

def search(request):
    query = request.GET.get('q', '').lower()
    results = {'industries': [], 'bots': [], 'services': []}
    if query:
        for ind in INDUSTRIES:
            if query in ind['name'].lower():
                results['industries'].append(ind)
        for bot in BOTS:
            if query in bot['name'].lower():
                results['bots'].append(bot)
        for svc in SERVICES:
            if query in svc['name'].lower():
                results['services'].append(svc)
    return render(request, 'pages/search.html', {'query': query, 'results': results})
