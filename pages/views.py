# Extended views.py with all industries and bots
from django.shortcuts import render
from django.http import Http404

INDUSTRIES = [
    {'name': 'E-Commerce', 'icon': 'E-Commerce', 'slug': 'ecommerce-automation', 'url': '/industries/ecommerce-automation/'},
    {'name': 'Finance', 'icon': 'Finance', 'slug': 'finance-automation', 'url': '/industries/finance-automation/'},
    {'name': 'Healthcare', 'icon': 'Healthcare', 'slug': 'healthcare-automation', 'url': '/industries/healthcare-automation/'},
    {'name': 'Education', 'icon': 'Education', 'slug': 'education-automation', 'url': '/industries/education-automation/'},
    {'name': 'Real Estate', 'icon': 'Real Estate', 'slug': 'real-estate-automation', 'url': '/industries/real-estate-automation/'},
    {'name': 'Marketing', 'icon': 'Marketing', 'slug': 'marketing-automation', 'url': '/industries/marketing-automation/'},
    {'name': 'HR', 'icon': 'HR', 'slug': 'hr-automation', 'url': '/industries/hr-automation/'},
    {'name': 'Legal', 'icon': 'Legal', 'slug': 'legal-automation', 'url': '/industries/legal-automation/'},
    {'name': 'Manufacturing', 'icon': 'Manufacturing', 'slug': 'manufacturing-automation', 'url': '/industries/manufacturing-automation/'},
    {'name': 'Logistics', 'icon': 'Logistics', 'slug': 'logistics-supply-chain-automation', 'url': '/industries/logistics-supply-chain-automation/'},
    {'name': 'Banking', 'icon': 'Banking', 'slug': 'banking-fintech-automation', 'url': '/industries/banking-fintech-automation/'},
    {'name': 'Energy', 'icon': 'Energy', 'slug': 'energy-utilities-automation', 'url': '/industries/energy-utilities-automation/'},
    {'name': 'Travel', 'icon': 'Travel', 'slug': 'travel-automation', 'url': '/industries/travel-automation/'},
    {'name': 'Media', 'icon': 'Media', 'slug': 'media-creative-automation', 'url': '/industries/media-creative-automation/'},
    {'name': 'Government', 'icon': 'Government', 'slug': 'government-automation', 'url': '/industries/government-automation/'},
    {'name': 'Agriculture', 'icon': 'Agriculture', 'slug': 'agriculture-automation', 'url': '/industries/agriculture-automation/'},
    {'name': 'Security', 'icon': 'Security', 'slug': 'security-automation', 'url': '/industries/security-automation/'},
    {'name': 'Automotive', 'icon': 'Automotive', 'slug': 'automotive-automation', 'url': '/industries/automotive-automation/'},
    {'name': 'Retail', 'icon': 'Retail', 'slug': 'retail-automation', 'url': '/industries/retail-automation/'},
    {'name': 'Insurance', 'icon': 'Insurance', 'slug': 'insurance-automation', 'url': '/industries/insurance-automation/'},
    {'name': 'Pharmaceutical', 'icon': 'Pharmaceutical', 'slug': 'pharmaceutical-automation', 'url': '/industries/pharmaceutical-automation/'},
    {'name': 'Construction', 'icon': 'Construction', 'slug': 'construction-automation', 'url': '/industries/construction-automation/'},
    {'name': 'Telecommunications', 'icon': 'Telecommunications', 'slug': 'telecommunications-automation', 'url': '/industries/telecommunications-automation/'},
    {'name': 'Food & Beverage', 'icon': 'Food and Beverage', 'slug': 'food-beverage-automation', 'url': '/industries/food-beverage-automation/'},
    {'name': 'Non-Profit', 'icon': 'Non-Profit', 'slug': 'non-profit-automation', 'url': '/industries/non-profit-automation/'},
    {'name': 'Sports', 'icon': 'Sports', 'slug': 'sports-automation', 'url': '/industries/sports-automation/'},
    {'name': 'Entertainment', 'icon': 'Entertainment', 'slug': 'entertainment-automation', 'url': '/industries/entertainment-automation/'},
    {'name': 'Transportation', 'icon': 'Transportation', 'slug': 'transportation-automation', 'url': '/industries/transportation-automation/'},
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
    {'name': 'Sentiment Analysis', 'slug': 'sentiment-analysis-bot', 'description': 'Brand monitoring AI', 'url': '/services/bots/sentiment-analysis-bot/'},
    {'name': 'Lead Scoring', 'slug': 'lead-scoring-bot', 'description': 'Predictive lead scoring', 'url': '/services/bots/lead-scoring-bot/'},
    {'name': 'Price Optimization', 'slug': 'price-optimization-bot', 'description': 'Dynamic pricing AI', 'url': '/services/bots/price-optimization-bot/'},
    {'name': 'Competitor Analysis', 'slug': 'competitor-analysis-bot', 'description': 'Market intelligence', 'url': '/services/bots/competitor-analysis-bot/'},
    {'name': 'Content Generation', 'slug': 'content-generation-bot', 'description': 'AI content creation', 'url': '/services/bots/content-generation-bot/'},
    {'name': 'SEO Optimization', 'slug': 'seo-optimization-bot', 'description': 'Search ranking AI', 'url': '/services/bots/seo-optimization-bot/'},
    {'name': 'Chatbot Builder', 'slug': 'chatbot-builder-bot', 'description': 'No-code bot creation', 'url': '/services/bots/chatbot-builder-bot/'},
    {'name': 'Translation Bot', 'slug': 'translation-bot', 'description': 'Multilingual translation', 'url': '/services/bots/translation-bot/'},
    {'name': 'Contract Review', 'slug': 'contract-review-bot', 'description': 'Legal document AI', 'url': '/services/bots/contract-review-bot/'},
    {'name': 'Debt Collection', 'slug': 'debt-collection-bot', 'description': 'AI collections agent', 'url': '/services/bots/debt-collection-bot/'},
    {'name': 'Loan Processing', 'slug': 'loan-processing-bot', 'description': 'Automated lending', 'url': '/services/bots/loan-processing-bot/'},
    {'name': 'Risk Assessment', 'slug': 'risk-assessment-bot', 'description': 'Credit risk AI', 'url': '/services/bots/risk-assessment-bot/'},
    {'name': 'Tax Preparation', 'slug': 'tax-preparation-bot', 'description': 'Automated tax filing', 'url': '/services/bots/tax-preparation-bot/'},
    {'name': 'Budget Forecasting', 'slug': 'budget-forecasting-bot', 'description': 'Financial planning AI', 'url': '/services/bots/budget-forecasting-bot/'},
    {'name': 'Supply Chain Bot', 'slug': 'supply-chain-bot', 'description': 'Logistics AI', 'url': '/services/bots/supply-chain-bot/'},
    {'name': 'Route Optimization', 'slug': 'route-optimization-bot', 'description': 'Delivery planning AI', 'url': '/services/bots/route-optimization-bot/'},
    {'name': 'Warehouse Bot', 'slug': 'warehouse-bot', 'description': 'Inventory management AI', 'url': '/services/bots/warehouse-bot/'},
    {'name': 'Quality Control', 'slug': 'quality-control-bot', 'description': 'AI inspection system', 'url': '/services/bots/quality-control-bot/'},
    {'name': 'Predictive Maintenance', 'slug': 'predictive-maintenance-bot', 'description': 'Equipment AI', 'url': '/services/bots/predictive-maintenance-bot/'},
    {'name': 'Patient Scheduling', 'slug': 'patient-scheduling-bot', 'description': 'Medical appointment AI', 'url': '/services/bots/patient-scheduling-bot/'},
    {'name': 'Medical Coding', 'slug': 'medical-coding-bot', 'description': 'ICD-10 coding AI', 'url': '/services/bots/medical-coding-bot/'},
    {'name': 'Drug Interaction', 'slug': 'drug-interaction-bot', 'description': 'Pharmacy safety AI', 'url': '/services/bots/drug-interaction-bot/'},
    {'name': 'Claims Triage', 'slug': 'claims-triage-bot', 'description': 'Insurance routing AI', 'url': '/services/bots/claims-triage-bot/'},
    {'name': 'Insurance Fraud', 'slug': 'insurance-fraud-bot', 'description': 'Claim fraud detection', 'url': '/services/bots/insurance-fraud-bot/'},
    {'name': 'Property Appraisal', 'slug': 'property-appraisal-bot', 'description': 'Real estate valuation AI', 'url': '/services/bots/property-appraisal-bot/'},
    {'name': 'Tenant Screening', 'slug': 'tenant-screening-bot', 'description': 'Rental application AI', 'url': '/services/bots/tenant-screening-bot/'},
    {'name': 'Lease Management', 'slug': 'lease-management-bot', 'description': 'Contract automation', 'url': '/services/bots/lease-management-bot/'},
    {'name': 'Recruitment Marketing', 'slug': 'recruitment-marketing-bot', 'description': 'Job posting AI', 'url': '/services/bots/recruitment-marketing-bot/'},
    {'name': 'Onboarding Bot', 'slug': 'onboarding-bot', 'description': 'Employee onboarding AI', 'url': '/services/bots/onboarding-bot/'},
    {'name': 'Performance Review', 'slug': 'performance-review-bot', 'description': 'Review analysis AI', 'url': '/services/bots/performance-review-bot/'},
    {'name': 'Attendance Bot', 'slug': 'attendance-bot', 'description': 'Time management AI', 'url': '/services/bots/attendance-bot/'},
    {'name': 'Payroll Bot', 'slug': 'payroll-bot', 'description': 'Automated payroll', 'url': '/services/bots/payroll-bot/'},
    {'name': 'Benefits Bot', 'slug': 'benefits-bot', 'description': 'Benefits management AI', 'url': '/services/bots/benefits-bot/'},
    {'name': 'Knowledge Base', 'slug': 'knowledge-base-bot', 'description': 'Internal KB assistant', 'url': '/services/bots/knowledge-base-bot/'},
    {'name': 'IT Ticket Bot', 'slug': 'it-ticket-bot', 'description': 'Help desk automation', 'url': '/services/bots/it-ticket-bot/'},
    {'name': 'Security Monitoring', 'slug': 'security-monitoring-bot', 'description': 'Threat detection AI', 'url': '/services/bots/security-monitoring-bot/'},
    {'name': 'Access Control', 'slug': 'access-control-bot', 'description': 'Identity management AI', 'url': '/services/bots/access-control-bot/'},
]

INDUSTRY_DATA = {
    'ecommerce-automation': {
        'name': 'E-Commerce Automation', 'icon': 'E-Commerce', 'description': 'Transform your online store with AI-powered automation. From inventory management to customer support, we streamline every aspect of your e-commerce operations.',
        'problems': ['Manual inventory tracking errors', 'Slow customer response times', 'Complex order processing', 'Cart abandonment issues', 'Personalization at scale challenges'],
        'solutions': ['AI-powered inventory prediction', 'Intelligent chatbots for support', 'Automated order processing', 'Personalized product recommendations', 'Dynamic pricing automation'],
        'bots': ['product-scraping-bot', 'inventory-prediction-bot', 'customer-support-bot', 'lead-qualification-bot']
    },
    'finance-automation': {
        'name': 'Finance and Banking Automation', 'icon': 'Finance', 'description': 'Revolutionize financial operations with intelligent automation. Automate invoicing, fraud detection, and financial reporting.',
        'problems': ['Manual invoice processing', 'Complex reconciliation tasks', 'Slow financial reporting', 'Fraud detection limitations', 'Compliance management burden'],
        'solutions': ['Invoice OCR automation', 'Automated reconciliation', 'Real-time financial dashboards', 'AI fraud detection systems', 'Compliance automation'],
        'bots': ['invoice-processing-bot', 'expense-processing-bot', 'fraud-detection-bot', 'compliance-monitoring-bot']
    },
    'healthcare-automation': {
        'name': 'Healthcare Automation', 'icon': 'Healthcare', 'description': 'Streamline healthcare operations with AI automation. Improve patient care, administrative efficiency, and diagnostic accuracy.',
        'problems': ['Administrative overhead', 'Appointment scheduling chaos', 'Medical transcription errors', 'Patient data management', 'Insurance claim processing'],
        'solutions': ['Smart appointment scheduling', 'AI medical transcription', 'EMR automation', 'Patient triage AI', 'Insurance claim automation'],
        'bots': ['patient-triage-bot', 'claim-processing-bot']
    },
    'education-automation': {
        'name': 'Education Automation', 'icon': 'Education', 'description': 'Transform educational institutions with AI automation. Automate grading, admissions, and student engagement.',
        'problems': ['Manual grading processes', 'Administrative overhead', 'Student engagement challenges', 'Admissions processing delays', 'Curriculum management'],
        'solutions': ['AI-powered grading', 'Automated admissions', 'Student engagement analytics', 'Personalized learning paths', 'Administrative automation'],
        'bots': []
    },
    'real-estate-automation': {
        'name': 'Real Estate Automation', 'icon': 'Real Estate', 'description': 'Revolutionize property management with AI automation. Automate lead qualification, property matching, and lease management.',
        'problems': ['Manual lead management', 'Slow response times', 'Property matching inefficiencies', 'Lease management overhead', 'Maintenance scheduling'],
        'solutions': ['AI lead qualification', 'Intelligent property matching', 'Automated lease management', 'Predictive maintenance', 'Virtual property tours'],
        'bots': ['lead-qualification-bot']
    },
    'marketing-automation': {
        'name': 'Marketing Automation', 'icon': 'Marketing', 'description': 'Supercharge your marketing with AI automation. Automate campaigns, content creation, and lead nurturing.',
        'problems': ['Manual campaign management', 'Content creation bottlenecks', 'Lead nurturing inefficiencies', 'A/B testing time-consuming', 'Social media management overhead'],
        'solutions': ['Automated campaign management', 'AI content generation', 'Personalized lead nurturing', 'Automated A/B testing', 'Social media automation'],
        'bots': ['email-automation-bot', 'social-media-bot', 'lead-qualification-bot']
    },
    'hr-automation': {
        'name': 'HR Automation', 'icon': 'HR', 'description': 'Streamline HR operations with AI automation. Automate recruiting, onboarding, and performance management.',
        'problems': ['Manual resume screening', 'Slow hiring processes', 'Onboarding inefficiencies', 'Performance review bottlenecks', 'Employee engagement tracking'],
        'solutions': ['AI resume screening', 'Automated interview scheduling', 'Digital onboarding', 'Performance analytics', 'Employee sentiment analysis'],
        'bots': ['resume-screening-bot', 'meeting-booking-bot']
    },
    'legal-automation': {
        'name': 'Legal Automation', 'icon': 'Legal', 'description': 'Transform legal operations with AI automation. Automate contract review, research, and document management.',
        'problems': ['Manual contract review', 'Legal research time-consuming', 'Document management chaos', 'Compliance tracking', 'Case management overhead'],
        'solutions': ['AI contract analysis', 'Automated legal research', 'Document automation', 'Compliance monitoring', 'Case management systems'],
        'bots': []
    },
    'manufacturing-automation': {
        'name': 'Manufacturing Automation', 'icon': 'Manufacturing', 'description': 'Optimize production with AI automation. Automate quality control, predictive maintenance, and inventory management.',
        'problems': ['Quality control inefficiencies', 'Unexpected downtime', 'Inventory management challenges', 'Production planning delays', 'Supply chain disruptions'],
        'solutions': ['AI quality inspection', 'Predictive maintenance', 'Smart inventory management', 'Production scheduling automation', 'Supply chain optimization'],
        'bots': []
    },
    'logistics-supply-chain-automation': {
        'name': 'Logistics and Supply Chain Automation', 'icon': 'Logistics', 'description': 'Optimize logistics with AI automation. Automate route planning, warehouse management, and demand forecasting.',
        'problems': ['Route planning inefficiencies', 'Warehouse management challenges', 'Demand forecasting inaccuracies', 'Shipment tracking overhead', 'Procurement delays'],
        'solutions': ['AI route optimization', 'Warehouse automation', 'Demand forecasting AI', 'Real-time shipment tracking', 'Automated procurement'],
        'bots': []
    },
    'banking-fintech-automation': {
        'name': 'Banking and Fintech Automation', 'icon': 'Banking', 'description': 'Transform banking operations with AI automation. Automate KYC, loan processing, and fraud detection.',
        'problems': ['KYC processing delays', 'Loan approval bottlenecks', 'Fraud detection limitations', 'Customer onboarding challenges', 'Compliance reporting'],
        'solutions': ['Automated KYC verification', 'AI-powered loan processing', 'Real-time fraud detection', 'Digital onboarding', 'Compliance automation'],
        'bots': ['kyc-verification-bot', 'fraud-detection-bot', 'claim-processing-bot']
    },
    'energy-utilities-automation': {
        'name': 'Energy and Utilities Automation', 'icon': 'Energy', 'description': 'Optimize energy operations with AI automation. Automate grid management, meter reading, and maintenance.',
        'problems': ['Grid management complexities', 'Manual meter reading', 'Maintenance scheduling challenges', 'Energy forecasting inaccuracies', 'Outage response delays'],
        'solutions': ['Smart grid management', 'Automated meter reading', 'Predictive maintenance', 'Energy demand forecasting', 'Outage management automation'],
        'bots': []
    },
    'travel-automation': {
        'name': 'Travel Automation', 'icon': 'Travel', 'description': 'Transform travel operations with AI automation. Automate booking, customer service, and itinerary management.',
        'problems': ['Booking management overhead', 'Customer service bottlenecks', 'Itinerary planning challenges', 'Inventory management', 'Revenue management'],
        'solutions': ['Automated booking management', 'AI customer service', 'Smart itinerary planning', 'Inventory optimization', 'Dynamic pricing'],
        'bots': []
    },
    'media-creative-automation': {
        'name': 'Media and Creative Automation', 'icon': 'Media', 'description': 'Accelerate content creation with AI automation. Automate transcription, translation, and publishing.',
        'problems': ['Content creation bottlenecks', 'Transcription time-consuming', 'Translation delays', 'Publishing workflow inefficiencies', 'Copyright monitoring'],
        'solutions': ['AI content generation', 'Automated transcription', 'Machine translation', 'Publishing automation', 'Copyright detection'],
        'bots': []
    },
    'government-automation': {
        'name': 'Government Automation', 'icon': 'Government', 'description': 'Modernize government services with AI automation. Automate citizen services, document verification, and compliance.',
        'problems': ['Citizen service delays', 'Document verification bottlenecks', 'Compliance reporting challenges', 'Public grievance handling', 'License processing'],
        'solutions': ['Digital citizen services', 'Automated document verification', 'Compliance reporting automation', 'Grievance management AI', 'License automation'],
        'bots': ['kyc-verification-bot', 'compliance-monitoring-bot']
    },
    'agriculture-automation': {
        'name': 'Agriculture Automation', 'icon': 'Agriculture', 'description': 'Revolutionize agriculture with AI automation. Automate crop monitoring, irrigation, and yield prediction.',
        'problems': ['Crop monitoring challenges', 'Irrigation inefficiencies', 'Yield prediction difficulties', 'Pest detection delays', 'Market pricing uncertainty'],
        'solutions': ['AI crop monitoring', 'Smart irrigation', 'Yield prediction AI', 'Pest detection automation', 'Market price forecasting'],
        'bots': []
    },
    'security-automation': {
        'name': 'Security Automation', 'icon': 'Security', 'description': 'Enhance security with AI automation. Automate threat detection, access control, and incident response.',
        'problems': ['Threat detection limitations', 'Access control inefficiencies', 'Incident response delays', 'Monitoring overhead', 'Compliance gaps'],
        'solutions': ['AI threat detection', 'Automated access control', 'Incident response automation', '24/7 monitoring', 'Security compliance automation'],
        'bots': ['fraud-detection-bot', 'compliance-monitoring-bot']
    },
    'automotive-automation': {
        'name': 'Automotive Automation', 'icon': 'Automotive', 'description': 'Transform automotive operations with AI automation. Automate manufacturing, inventory, and customer service.',
        'problems': ['Manufacturing inefficiencies', 'Inventory management challenges', 'Customer service bottlenecks', 'Quality control delays', 'Supply chain disruptions'],
        'solutions': ['AI manufacturing automation', 'Smart inventory management', 'AI customer service', 'Quality inspection automation', 'Supply chain optimization'],
        'bots': []
    },
}

BOTS_DATA = {
    'lead-qualification-bot': {
        'name': 'Lead Qualification Bot', 'industry': 'Sales and Marketing', 'description': 'Automatically qualify leads 24/7 with AI-powered conversation bots. Score leads, gather info, and route to sales team.',
        'features': ['Automated lead scoring', 'Custom qualification questions', 'CRM integration', 'Multi-channel deployment', 'Real-time notifications'],
        'use_cases': ['E-Commerce', 'SaaS', 'Real Estate', 'Finance', 'B2B Sales']
    },
    'invoice-processing-bot': {
        'name': 'Invoice Processing Bot', 'industry': 'Finance and Accounting', 'description': 'Automate invoice extraction, validation, and processing. Reduce manual work by 90% with AI-powered OCR.',
        'features': ['OCR invoice extraction', 'Automatic validation', 'Approval workflow', 'Payment tracking', 'Audit trail'],
        'use_cases': ['Finance', 'Healthcare', 'Manufacturing', 'Retail']
    },
    'customer-support-bot': {
        'name': 'Customer Support Bot', 'industry': 'Customer Service', 'description': 'AI-powered chatbot for 24/7 customer support. Handle common queries and escalate complex issues.',
        'features': ['Natural language understanding', 'Multi-language support', 'Knowledge base integration', 'Ticket creation', 'Escalation management'],
        'use_cases': ['E-Commerce', 'SaaS', 'Finance', 'Healthcare']
    },
    'fraud-detection-bot': {
        'name': 'Fraud Detection Bot', 'industry': 'Security and Finance', 'description': 'Real-time fraud detection using AI. Identify suspicious patterns and prevent fraudulent transactions.',
        'features': ['Real-time transaction monitoring', 'Pattern recognition', 'Risk scoring', 'Alert system', 'Custom rules'],
        'use_cases': ['Banking', 'E-Commerce', 'Finance', 'Insurance']
    },
    'product-scraping-bot': {
        'name': 'Product Scraping Bot', 'industry': 'E-Commerce', 'description': 'Automated product data extraction from competitor websites. Monitor prices, inventory, and product details.',
        'features': ['Price monitoring', 'Inventory tracking', 'Competitor analysis', 'Data export', 'Scheduled scraping'],
        'use_cases': ['E-Commerce', 'Retail', 'Price Comparison']
    },
    'inventory-prediction-bot': {
        'name': 'Inventory Prediction Bot', 'industry': 'Supply Chain', 'description': 'AI-powered demand forecasting for optimal inventory management. Predict stock needs and prevent shortages.',
        'features': ['Demand forecasting', 'Reorder point optimization', 'Seasonal analysis', 'Alert system', 'Reporting dashboard'],
        'use_cases': ['E-Commerce', 'Retail', 'Manufacturing']
    },
    'resume-screening-bot': {
        'name': 'Resume Screening Bot', 'industry': 'HR and Recruiting', 'description': 'Automated candidate screening using AI. Rank resumes and identify best matches for open positions.',
        'features': ['Keyword matching', 'Skills assessment', 'Experience analysis', 'Ranking system', 'Interview scheduling'],
        'use_cases': ['HR', 'Recruiting', 'Staffing']
    },
    'meeting-booking-bot': {
        'name': 'Meeting Booking Bot', 'industry': 'Sales and Operations', 'description': 'Automated meeting scheduling across time zones. Find optimal times and manage calendars.',
        'features': ['Calendar integration', 'Time zone handling', 'Automated reminders', 'Rescheduling', 'Booking analytics'],
        'use_cases': ['Sales', 'HR', 'Operations']
    },
    'social-media-bot': {
        'name': 'Social Media Bot', 'industry': 'Marketing', 'description': 'Automate social media content posting and engagement. Schedule posts and respond to comments.',
        'features': ['Post scheduling', 'Content curation', 'Engagement automation', 'Analytics', 'Multi-platform'],
        'use_cases': ['Marketing', 'Brand Management']
    },
    'email-automation-bot': {
        'name': 'Email Automation Bot', 'industry': 'Marketing', 'description': 'Automated email campaign management. Create, send, and track email campaigns at scale.',
        'features': ['Campaign creation', 'Personalization', 'A/B testing', 'Analytics', 'Automation triggers'],
        'use_cases': ['Marketing', 'Sales', 'Customer Retention']
    },
    'data-entry-bot': {
        'name': 'Data Entry Bot', 'industry': 'Operations', 'description': 'Automated data input and validation. Extract data from documents and enter into systems.',
        'features': ['OCR extraction', 'Data validation', 'Format conversion', 'Error handling', 'Audit logs'],
        'use_cases': ['Finance', 'Healthcare', 'Legal']
    },
    'expense-processing-bot': {
        'name': 'Expense Processing Bot', 'industry': 'Finance', 'description': 'Automated expense receipt processing and categorization. Extract details and reconcile expenses.',
        'features': ['Receipt scanning', 'Auto-categorization', 'Policy compliance', 'Approval workflow', 'Reporting'],
        'use_cases': ['Finance', 'HR', 'Operations']
    },
    'kyc-verification-bot': {
        'name': 'KYC Verification Bot', 'industry': 'Banking and Finance', 'description': 'Automated Know Your Customer verification. Validate identities and documents in seconds.',
        'features': ['ID verification', 'Document validation', 'Biometric matching', 'Sanctions screening', 'Compliance reports'],
        'use_cases': ['Banking', 'Fintech', 'Government']
    },
    'claim-processing-bot': {
        'name': 'Claim Processing Bot', 'industry': 'Insurance', 'description': 'Automated insurance claims processing. Validate claims and accelerate approvals.',
        'features': ['Claim intake', 'Validation automation', 'Fraud detection', 'Approval routing', 'Status tracking'],
        'use_cases': ['Insurance', 'Healthcare']
    },
    'patient-triage-bot': {
        'name': 'Patient Triage Bot', 'industry': 'Healthcare', 'description': 'AI-powered patient triage and symptom assessment. Guide patients to appropriate care.',
        'features': ['Symptom assessment', 'Urgency classification', 'Appointment scheduling', 'HIPAA compliant', 'Integration with EMR'],
        'use_cases': ['Healthcare', 'Telemedicine']
    },
    'compliance-monitoring-bot': {
        'name': 'Compliance Monitoring Bot', 'industry': 'Legal and Finance', 'description': 'Automated regulatory compliance monitoring. Track changes and ensure adherence.',
        'features': ['Regulation tracking', 'Gap analysis', 'Alert system', 'Audit preparation', 'Reporting'],
        'use_cases': ['Banking', 'Healthcare', 'Government']
    }
}

def home(request):
    return render(request, 'pages/home.html', {'industries': INDUSTRIES, 'services': SERVICES, 'bots': BOTS})

def industries_list(request):
    return render(request, 'pages/industries_list.html', {'industries': INDUSTRIES})

def industry_detail(request, industry_slug):
    if industry_slug not in INDUSTRY_DATA:
        raise Http404("Industry not found")
    industry = INDUSTRY_DATA[industry_slug]
    return render(request, 'pages/industry_detail.html', {'industry': industry, 'slug': industry_slug})

def services_list(request):
    return render(request, 'pages/services_list.html', {'services': SERVICES})

def service_detail(request, service_slug):
    return render(request, 'pages/service_detail.html', {'slug': service_slug})

def bot_detail(request, bot_slug):
    if bot_slug not in BOTS_DATA:
        raise Http404("Bot not found")
    bot = BOTS_DATA[bot_slug]
    return render(request, 'pages/bot_detail.html', {'bot': bot, 'slug': bot_slug})

def case_studies(request):
    return render(request, 'pages/case_studies.html')

def pricing(request):
    pricing_tiers = [
        {'name': 'Starter', 'price': '499', 'description': 'Perfect for small businesses', 'features': ['1 AI Bot', 'Basic integration', 'Email support', 'Monthly reports']},
        {'name': 'Professional', 'price': '1499', 'description': 'For growing businesses', 'features': ['3 AI Bots', 'Advanced integrations', 'Priority support', 'Weekly reports', 'Custom training']},
        {'name': 'Enterprise', 'price': 'Custom', 'description': 'For large organizations', 'features': ['Unlimited bots', 'Full integrations', '24/7 support', 'Real-time analytics', 'Dedicated manager']},
    ]
    return render(request, 'pages/pricing.html', {'pricing_tiers': pricing_tiers})

def contact(request):
    return render(request, 'pages/contact.html')

def case_study_detail(request, slug):
    return render(request, 'pages/case_study_detail.html', {'slug': slug})

def blog_list(request):
    return render(request, 'pages/blog_list.html', {'posts': [], 'categories': []})

def blog_detail(request, slug):
    return render(request, 'pages/blog_detail.html', {'slug': slug})

def sitemap_xml(request):
    from django.http import HttpResponse
    sites = []
    for ind in INDUSTRIES:
        sites.append(f"https://example.com/industries/{ind['slug']}/")
    for bot in BOTS:
        sites.append(f"https://example.com/services/bots/{bot['slug']}/")
    xml = '<?xml version="1.0"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    xml += '<url><loc>https://example.com/</loc><priority>1.0</priority></url>\n'
    for site in sites:
        xml += f'<url><loc>{site}</loc><priority>0.8</priority></url>\n'
    xml += '</urlset>'
    return HttpResponse(xml, content_type='application/xml')

def robots_txt(request):
    from django.http import HttpResponse
    return HttpResponse("User-agent: *\nAllow: /\nSitemap: https://example.com/sitemap.xml\n", content_type='text/plain')

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
    return render(request, 'pages/search.html', {'query': query, 'results': results})
