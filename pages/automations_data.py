# AI Automation Services Data
# 28 Categories with n8n workflow specs and Python API specs

AUTOMATIONS = [
    {
        'id': 1,
        'name': 'Business Process Automation',
        'slug': 'business-process-automation',
        'icon': '⚙️',
        'color': '#3b82f6',
        'description': 'Streamline workflows, automate approvals, and orchestrate complex business processes across your organization.',
        'full_description': '''
            Business Process Automation (BPA) transforms how your organization operates by automating repetitive workflows, 
            eliminating manual bottlenecks, and ensuring consistent process execution. From simple approval chains to 
            complex multi-department workflows, we build scalable solutions that reduce errors and save time.
        ''',
        'services': [
            'Workflow Automation', 'Process Orchestration', 'Approval Flow Automation',
            'Task Assignment Automation', 'Cross-department Process Automation',
            'Document Routing Automation', 'Form Processing Automation', 'Internal Operations Bots', 'SOP Automation', 'Back-office Automation'
        ],
        'use_cases': [
            'Employee onboarding workflows', 'Purchase approval chains', 'Document routing and approval',
            'SOP execution and compliance', 'Multi-department handoffs', 'Leave request approvals'
        ],
        'tools': ['n8n', 'Zapier', 'Power Automate', 'Make', 'Camunda'],
        'n8n_workflow': {
            'trigger': 'Webhook / Schedule',
            'nodes': ['Webhook', 'IF', 'Slack', 'Email', 'Google Sheets', 'HTTP Request'],
            'complexity': 'Medium',
            'estimated_hours': 8
        },
        'python_api': {
            'endpoints': ['/api/workflows/', '/api/tasks/', '/api/approvals/'],
            'libraries': ['FastAPI', 'Celery', 'Pydantic'],
            'ai_features': None
        },
        'pricing_tier': 'Mid-market',
        'pricing': {'start': '$499/mo', 'enterprise': 'Custom'}
    },
    {
        'id': 2,
        'name': 'Robotic Process Automation',
        'slug': 'robotic-process-automation',
        'icon': '🤖',
        'color': '#8b5cf6',
        'description': 'Automate repetitive tasks, legacy system interactions, and UI-based processes with intelligent RPA bots.',
        'full_description': '''
            Robotic Process Automation (RPA) uses software robots to mimic human actions on computer systems. 
            Perfect for automating legacy systems that lack APIs, data entry tasks, and repetitive processes 
            that require UI interaction.
        ''',
        'services': [
            'UI-based Task Automation', 'Legacy System Automation', 'Desktop Automation Bots',
            'Web Automation Bots', 'Invoice Processing Bots', 'Data Entry Bots',
            'Reconciliation Bots', 'Exception Handling Bots', 'Human-in-the-loop Bots', 'Unattended Automation Bots'
        ],
        'use_cases': [
            'Invoice processing from PDFs', 'Data entry from emails', 'Legacy ERP automation',
            'System-to-system data migration', 'Daily report generation'
        ],
        'tools': ['UiPath', 'Automation Anywhere', 'Blue Prism', 'Python Selenium', 'Playwright'],
        'n8n_workflow': {
            'trigger': 'Schedule / Webhook',
            'nodes': ['Schedule Trigger', 'Read Binary Files', 'Python Code', 'HTTP Request', 'Google Sheets'],
            'complexity': 'High',
            'estimated_hours': 24
        },
        'python_api': {
            'endpoints': ['/api/rpa/tasks/', '/api/rpa/bots/', '/api/rpa/executions/'],
            'libraries': ['FastAPI', 'Selenium', 'Playwright', 'PyPDF2', 'python-docx'],
            'ai_features': 'OCR for document processing'
        },
        'pricing_tier': 'Enterprise',
        'pricing': {'start': '$1999/mo', 'enterprise': 'Custom'}
    },
    {
        'id': 3,
        'name': 'AI Chatbot & Conversational Automation',
        'slug': 'ai-chatbot-automation',
        'icon': '💬',
        'color': '#ec4899',
        'description': 'Build intelligent conversational agents for websites, messaging platforms, and voice interfaces.',
        'full_description': '''
            AI-powered chatbots and conversational agents provide 24/7 customer support, lead qualification, 
            and internal helpdesk capabilities. Using Large Language Models (LLMs), these bots understand context, 
            handle complex queries, and continuously improve from interactions.
        ''',
        'services': [
            'Website Chatbots', 'WhatsApp Bots', 'Telegram Bots', 'Messenger Bots',
            'Voice Bots (IVR)', 'Multilingual Chatbots', 'Sales Conversation Bots',
            'Customer Support Bots', 'Internal Employee Bots', 'AI Receptionist Bots'
        ],
        'use_cases': [
            'Website visitor qualification', 'Customer support 24/7', 'Internal HR helpdesk',
            'Appointment scheduling', 'Lead nurturing', 'FAQ handling'
        ],
        'tools': ['Voiceflow', 'Botpress', 'Rasa', 'LangChain', 'Custom LLM', 'Twilio', 'WhatsApp API'],
        'n8n_workflow': {
            'trigger': 'Webhook from Chat Platform',
            'nodes': ['Webhook', 'LangChain Agent', 'Memory', 'Vector Store', 'Slack/Email'],
            'complexity': 'High',
            'estimated_hours': 32
        },
        'python_api': {
            'endpoints': ['/api/chat/', '/api/conversations/', '/api/chatbots/'],
            'libraries': ['FastAPI', 'LangChain', 'OpenAI', 'HuggingFace', 'ChromaDB'],
            'ai_features': 'LLM conversation, RAG, intent recognition, sentiment analysis'
        },
        'pricing_tier': 'All',
        'pricing': {'start': '$299/mo', 'enterprise': 'Custom'}
    },
    {
        'id': 4,
        'name': 'Sales Automation',
        'slug': 'sales-automation',
        'icon': '📈',
        'color': '#10b981',
        'description': 'Automate your entire sales pipeline from lead capture to deal closure and follow-ups.',
        'full_description': '''
            Sales automation eliminates manual follow-ups, streamlines pipeline management, and ensures 
            no lead falls through the cracks. From automated lead scoring to proposal generation, 
            empower your sales team to focus on closing deals.
        ''',
        'services': [
            'Lead Qualification Automation', 'CRM Workflow Automation', 'Sales Pipeline Automation',
            'Follow-up Automation', 'Proposal Generation Automation', 'Quote Generation Bots',
            'Sales Forecasting AI', 'Deal Scoring AI', 'Outbound Email Automation', 'Meeting Booking Automation'
        ],
        'use_cases': [
            'Lead scoring and qualification', 'Automatic follow-up sequences', 'Proposal generation',
            'Meeting scheduler', 'Deal pipeline updates', 'Sales forecasting'
        ],
        'tools': ['HubSpot', 'Salesforce', 'Pipedrive', 'Zapier', 'n8n', 'Apollo', 'Calendly'],
        'n8n_workflow': {
            'trigger': 'CRM Webhook / Schedule',
            'nodes': ['Webhook', 'CRM', 'Email', 'AI Agent', 'Calendar', 'Slack'],
            'complexity': 'Medium',
            'estimated_hours': 16
        },
        'python_api': {
            'endpoints': ['/api/leads/', '/api/deals/', '/api/forecasting/'],
            'libraries': ['FastAPI', 'Pandas', 'Scikit-learn', 'OpenAI'],
            'ai_features': 'Lead scoring model, deal prediction, sentiment analysis'
        },
        'pricing_tier': 'Mid-market',
        'pricing': {'start': '$399/mo', 'enterprise': 'Custom'}
    },
    {
        'id': 5,
        'name': 'Marketing Automation',
        'slug': 'marketing-automation',
        'icon': '📣',
        'color': '#f59e0b',
        'description': 'Create, launch, and optimize marketing campaigns across all channels with AI-powered automation.',
        'full_description': '''
            Marketing automation handles repetitive campaigns, personalizes content at scale, and nurtures 
            leads through the funnel. From email sequences to social media posting, automate your marketing 
            to achieve more with less effort.
        ''',
        'services': [
            'Campaign Automation', 'Email Marketing Automation', 'Social Media Automation',
            'Content Publishing Automation', 'SEO Content Automation', 'Ad Copy Automation',
            'Personalization Engines', 'A/B Testing Automation', 'Retargeting Automation', 'Customer Journey Automation'
        ],
        'use_cases': [
            'Email drip campaigns', 'Social media scheduling', 'Ad campaign optimization',
            'Lead nurturing flows', 'AB testing', 'Personalized content'
        ],
        'tools': ['Mailchimp', 'HubSpot', 'Klaviyo', 'Buffer', 'Zapier', 'n8n', 'Google Ads', 'Facebook Ads'],
        'n8n_workflow': {
            'trigger': 'Schedule / Webhook',
            'nodes': ['Schedule', 'HTTP Request', 'AI Agent', 'Email', 'Social Media', 'Google Sheets'],
            'complexity': 'Medium',
            'estimated_hours': 12
        },
        'python_api': {
            'endpoints': ['/api/campaigns/', '/api/content/', '/api/analytics/'],
            'libraries': ['FastAPI', 'OpenAI', 'Selenium', 'Pandas'],
            'ai_features': 'Ad copy generation, content personalization, A/B test analysis'
        },
        'pricing_tier': 'Mid-market',
        'pricing': {'start': '$299/mo', 'enterprise': 'Custom'}
    },
    {
        'id': 6,
        'name': 'Customer Support Automation',
        'slug': 'customer-support-automation',
        'icon': '🎧',
        'color': '#06b6d4',
        'description': 'Transform customer service with AI-powered ticketing, routing, and resolution automation.',
        'full_description': '''
            Customer support automation reduces response times, handles common queries instantly, and intelligently 
            routes complex issues to the right agents. Combine AI chatbots with workflow automation for 
            exceptional customer experiences.
        ''',
        'services': [
            'Ticket Classification Automation', 'Auto-reply Bots', 'Sentiment Analysis Automation',
            'Escalation Prediction', 'Refund Automation', 'Complaint Resolution Bots',
            'Support Analytics Automation', 'Call Summarization AI', 'Knowledge Base Automation', 'Omnichannel Support Automation'
        ],
        'use_cases': [
            'Ticket auto-routing', 'Instant FAQ responses', 'Refund processing',
            'Sentiment-based prioritization', 'Call summaries', 'Knowledge base search'
        ],
        'tools': ['Zendesk', 'Freshdesk', 'Intercom', 'OpenAI', 'LangChain', 'Twilio'],
        'n8n_workflow': {
            'trigger': 'Webhook from Support Platform',
            'nodes': ['Webhook', 'AI Agent', 'Sentiment Analysis', 'IF', 'Email/Slack', 'Zendesk'],
            'complexity': 'High',
            'estimated_hours': 20
        },
        'python_api': {
            'endpoints': ['/api/tickets/', '/api/responses/', '/api/analytics/'],
            'libraries': ['FastAPI', 'LangChain', 'OpenAI', 'TextBlob'],
            'ai_features': 'Sentiment analysis, auto-responses, escalation prediction, summarization'
        },
        'pricing_tier': 'All',
        'pricing': {'start': '$349/mo', 'enterprise': 'Custom'}
    },
    {
        'id': 7,
        'name': 'Finance & Accounting Automation',
        'slug': 'finance-automation',
        'icon': '💰',
        'color': '#14b8a6',
        'description': 'Automate invoicing, expense management, payroll, and financial reporting with AI.',
        'full_description': '''
            Finance automation streamlines accounts payable/receivable, reduces processing costs, and provides 
            real-time financial insights. From OCR invoice processing to cash flow prediction, automate 
            your finance operations for accuracy and speed.
        ''',
        'services': [
            'Invoice OCR Automation', 'Expense Automation', 'Payroll Automation',
            'Tax Calculation Automation', 'Financial Reporting Automation', 'Audit Automation',
            'Fraud Detection AI', 'Budget Forecasting AI', 'Cash-flow Prediction', 'Vendor Payment Automation'
        ],
        'use_cases': [
            'Invoice data extraction', 'Expense report processing', 'Automated reconciliation',
            'Financial reports', 'Fraud detection', 'Cash flow forecasting'
        ],
        'tools': ['QuickBooks', 'Xero', 'Stripe', 'Python', 'AWS Textract', 'Google Cloud Vision'],
        'n8n_workflow': {
            'trigger': 'Schedule / Email Webhook',
            'nodes': ['Email Read', 'OCR', 'AI Agent', 'Database', 'Accounting Software', 'Approval'],
            'complexity': 'High',
            'estimated_hours': 24
        },
        'python_api': {
            'endpoints': ['/api/invoices/', '/api/expenses/', '/api/reports/', '/api/forecasting/'],
            'libraries': ['FastAPI', 'Pandas', 'NumPy', 'Scikit-learn', 'AWS Textract', 'OpenCV'],
            'ai_features': 'OCR invoice extraction, fraud detection, cash flow prediction, anomaly detection'
        },
        'pricing_tier': 'Enterprise',
        'pricing': {'start': '$799/mo', 'enterprise': 'Custom'}
    },
    {
        'id': 8,
        'name': 'HR & Workforce Automation',
        'slug': 'hr-automation',
        'icon': '👥',
        'color': '#f97316',
        'description': 'Streamline recruitment, onboarding, attendance, and performance management with AI.',
        'full_description': '''
            HR automation transforms the employee lifecycle from hiring to offboarding. Automate repetitive 
            tasks like resume screening and interview scheduling, while using AI to gain insights into 
            workforce trends and employee sentiment.
        ''',
        'services': [
            'Resume Parsing AI', 'Candidate Screening Automation', 'Interview Scheduling Bots',
            'Onboarding Automation', 'Attendance Automation', 'Performance Review Automation',
            'Training Recommendation AI', 'Employee Sentiment Analysis', 'Exit Process Automation', 'Workforce Analytics Automation'
        ],
        'use_cases': [
            'Resume screening', 'Interview scheduling', 'Onboarding workflows',
            'Attendance tracking', 'Performance reviews', 'Employee surveys'
        ],
        'tools': ['BambooHR', 'Greenhouse', 'Lever', 'Zapier', 'n8n', 'Calendly', 'Slack'],
        'n8n_workflow': {
            'trigger': 'Schedule / Webhook',
            'nodes': ['Webhook', 'AI Resume Parser', 'Schedule', 'Email', 'Google Sheets', 'HRIS'],
            'complexity': 'Medium',
            'estimated_hours': 16
        },
        'python_api': {
            'endpoints': ['/api/candidates/', '/api/employees/', '/api/analytics/'],
            'libraries': ['FastAPI', 'Spacy', 'OpenAI', 'Pandas'],
            'ai_features': 'Resume parsing, candidate matching, sentiment analysis, workforce insights'
        },
        'pricing_tier': 'Mid-market',
        'pricing': {'start': '$449/mo', 'enterprise': 'Custom'}
    },
    {
        'id': 9,
        'name': 'IT & DevOps Automation',
        'slug': 'it-devops-automation',
        'icon': '🖥️',
        'color': '#6366f1',
        'description': 'Automate infrastructure, CI/CD pipelines, monitoring, and incident response.',
        'full_description': '''
            DevOps automation accelerates deployments, ensures consistent infrastructure, and reduces 
            MTTR (Mean Time To Recovery). From CI/CD pipelines to self-healing infrastructure, 
            automate your IT operations for speed and reliability.
        ''',
        'services': [
            'CI/CD Automation', 'Infrastructure Provisioning Automation', 'Cloud Resource Automation',
            'Log Monitoring Automation', 'Incident Response Automation', 'Auto-scaling Automation',
            'Backup Automation', 'Patch Management Automation', 'Security Monitoring Automation', 'DevOps Workflow Automation'
        ],
        'use_cases': [
            'Automated deployments', 'Infrastructure as code', 'Log aggregation',
            'Incident response', 'Auto-scaling', 'Backup verification'
        ],
        'tools': ['GitHub Actions', 'GitLab CI', 'Jenkins', 'Terraform', 'Ansible', 'Kubernetes', 'Datadog', 'PagerDuty'],
        'n8n_workflow': {
            'trigger': 'Git Webhook / Schedule',
            'nodes': ['GitHub Webhook', 'Build', 'Test', 'Deploy', 'Notify', 'Update Tracker'],
            'complexity': 'High',
            'estimated_hours': 32
        },
        'python_api': {
            'endpoints': ['/api/deployments/', '/api/metrics/', '/api/incidents/'],
            'libraries': ['FastAPI', 'Paramiko', 'Boto3', 'Docker', 'Kubectl'],
            'ai_features': 'Log analysis, incident prediction, auto-remediation'
        },
        'pricing_tier': 'Enterprise',
        'pricing': {'start': '$999/mo', 'enterprise': 'Custom'}
    },
    {
        'id': 10,
        'name': 'Data Automation & Intelligence',
        'slug': 'data-automation',
        'icon': '📊',
        'color': '#84cc16',
        'description': 'Extract, transform, load, and analyze data with intelligent automation pipelines.',
        'full_description': '''
            Data automation handles the entire data lifecycle - from extraction to analysis. Build robust 
            ETL pipelines, automate reporting, and leverage AI for predictive insights without manual 
            intervention.
        ''',
        'services': [
            'Data Extraction Automation', 'Web Scraping Automation', 'OCR Automation',
            'ETL Pipeline Automation', 'Data Validation Automation', 'Data Synchronization Automation',
            'Data Enrichment Automation', 'Reporting Automation', 'Dashboard Automation', 'Predictive Analytics Automation'
        ],
        'use_cases': [
            'Web data extraction', 'Report generation', 'Data sync between systems',
            'Data quality validation', 'Dashboard creation', 'Predictive models'
        ],
        'tools': ['Python', 'Apache Airflow', 'dbt', 'Fivetran', 'Pandas', 'Selenium', 'BeautifulSoup'],
        'n8n_workflow': {
            'trigger': 'Schedule / Webhook',
            'nodes': ['Schedule', 'HTTP Request', 'Scraper', 'Transform', 'Database', 'Report'],
            'complexity': 'Medium',
            'estimated_hours': 20
        },
        'python_api': {
            'endpoints': ['/api/data/', '/api/etl/', '/api/analytics/', '/api/predictions/'],
            'libraries': ['FastAPI', 'Pandas', 'NumPy', 'Scikit-learn', 'LangChain', 'BeautifulSoup', 'Selenium'],
            'ai_features': 'Data enrichment, predictive analytics, anomaly detection'
        },
        'pricing_tier': 'Mid-market',
        'pricing': {'start': '$599/mo', 'enterprise': 'Custom'}
    },
    {
        'id': 11,
        'name': 'AI & Machine Learning Automation',
        'slug': 'ai-ml-automation',
        'icon': '🧠',
        'color': '#d946ef',
        'description': 'Deploy, monitor, and scale AI models with automated MLOps pipelines.',
        'full_description': '''
            AI/ML automation (MLOps) streamlines the entire ML lifecycle from model development to deployment. 
            Automate training, monitoring, and retraining to keep your AI models accurate and performant 
            without manual intervention.
        ''',
        'services': [
            'Model Deployment Automation', 'Prediction System Automation', 'Recommendation Engine Automation',
            'NLP Workflow Automation', 'Computer Vision Automation', 'Speech-to-text Automation',
            'Text-to-speech Automation', 'Prompt Pipeline Automation', 'Vector Database Automation', 'Auto-ML Workflows'
        ],
        'use_cases': [
            'ML model deployment', 'Real-time predictions', 'Recommendation systems',
            'NLP pipelines', 'AutoML', 'Model monitoring'
        ],
        'tools': ['LangChain', 'Hugging Face', 'Weights & Biases', 'MLflow', 'Ray', 'Seldon', 'Kubeflow'],
        'n8n_workflow': {
            'trigger': 'Webhook / Schedule',
            'nodes': ['Webhook', 'ML Model', 'Preprocessing', 'Postprocessing', 'Database', 'Notify'],
            'complexity': 'Very High',
            'estimated_hours': 40
        },
        'python_api': {
            'endpoints': ['/api/models/', '/api/predictions/', '/api/training/', '/api/vector-search/'],
            'libraries': ['FastAPI', 'LangChain', 'LlamaIndex', 'HuggingFace', 'TensorFlow', 'PyTorch', 'Pinecone', 'Weaviate'],
            'ai_features': 'LLM orchestration, RAG, embeddings, fine-tuning, model serving'
        },
        'pricing_tier': 'Enterprise',
        'pricing': {'start': '$1499/mo', 'enterprise': 'Custom'}
    },
    {
        'id': 12,
        'name': 'Document & Content Automation',
        'slug': 'document-automation',
        'icon': '📄',
        'color': '#a855f7',
        'description': 'Generate, classify, process, and manage documents with AI-powered automation.',
        'full_description': '''
            Document automation eliminates manual document handling. From contract generation to 
            intelligent classification, use AI to process documents at scale while ensuring accuracy 
            and compliance.
        ''',
        'services': [
            'Document Classification AI', 'Contract Automation', 'Policy Automation',
            'Legal Document Automation', 'Report Generation Automation', 'Content Summarization AI',
            'Translation Automation', 'E-signature Automation', 'Document Compliance Automation', 'Knowledge Base Automation'
        ],
        'use_cases': [
            'Contract generation', 'Document classification', 'Report automation',
            'Translation', 'E-signatures', 'Compliance checking'
        ],
        'tools': ['DocuSign', 'PandaDoc', 'Python', 'LangChain', 'Google Translate API', 'AWS Textract'],
        'n8n_workflow': {
            'trigger': 'Webhook / Schedule',
            'nodes': ['Webhook', 'AI Document Parser', 'Transform', 'Template', 'E-sign', 'Store'],
            'complexity': 'Medium',
            'estimated_hours': 16
        },
        'python_api': {
            'endpoints': ['/api/documents/', '/api/contracts/', '/api/translate/', '/api/summarize/'],
            'libraries': ['FastAPI', 'LangChain', 'OpenAI', 'AWS Textract', 'PyPDF2', 'python-docx'],
            'ai_features': 'Document parsing, summarization, translation, classification'
        },
        'pricing_tier': 'Mid-market',
        'pricing': {'start': '$399/mo', 'enterprise': 'Custom'}
    },
    {
        'id': 13,
        'name': 'E-commerce Automation',
        'slug': 'ecommerce-automation',
        'icon': '🛒',
        'color': '#ef4444',
        'description': 'Automate product listings, inventory, orders, and customer retention for online stores.',
        'full_description': '''
            E-commerce automation handles the entire online retail operation. From product listings 
            to customer retention, automate workflows across multiple marketplaces while maintaining 
            inventory accuracy and delivering personalized experiences.
        ''',
        'services': [
            'Product Catalog Automation', 'Pricing Automation', 'Inventory Automation',
            'Order Processing Automation', 'Return & Refund Automation', 'Recommendation Engines',
            'Customer Retention Automation', 'Review Analysis Automation', 'Marketplace Integration Automation', 'Fulfillment Automation'
        ],
        'use_cases': [
            'Multi-channel listings', 'Dynamic pricing', 'Inventory sync',
            'Order processing', 'Customer retention', 'Review analysis'
        ],
        'tools': ['Shopify', 'WooCommerce', 'Amazon Seller', 'Zapier', 'n8n', 'Repricer', 'Yabi'],
        'n8n_workflow': {
            'trigger': 'Webhook / Schedule',
            'nodes': ['E-commerce Webhook', 'AI Agent', 'Inventory', 'Pricing', 'Orders', 'Email'],
            'complexity': 'High',
            'estimated_hours': 24
        },
        'python_api': {
            'endpoints': ['/api/products/', '/api/orders/', '/api/pricing/', '/api/recommendations/'],
            'libraries': ['FastAPI', 'Shopify API', 'Amazon SP-API', 'Scikit-learn'],
            'ai_features': 'Dynamic pricing, recommendations, demand forecasting, churn prediction'
        },
        'pricing_tier': 'All',
        'pricing': {'start': '$349/mo', 'enterprise': 'Custom'}
    },
    {
        'id': 14,
        'name': 'Manufacturing & Industrial Automation',
        'slug': 'manufacturing-automation',
        'icon': '🏭',
        'color': '#64748b',
        'description': 'Optimize production, quality, and supply chain with AI and IoT automation.',
        'full_description': '''
            Industrial automation combines IoT sensors, AI analytics, and robotics to optimize manufacturing. 
            From predictive maintenance to quality control, build smart factories that reduce downtime 
            and improve efficiency.
        ''',
        'services': [
            'Predictive Maintenance AI', 'Quality Inspection AI', 'Production Scheduling Automation',
            'Inventory Optimization', 'Supply Chain Automation', 'Machine Monitoring Automation',
            'Safety Monitoring AI', 'Energy Optimization Automation', 'IoT Data Automation', 'Industrial RPA Bots'
        ],
        'use_cases': [
            'Predictive maintenance', 'Quality inspection', 'Production planning',
            'IoT monitoring', 'Energy optimization', 'Supply chain visibility'
        ],
        'tools': ['Azure IoT', 'AWS IoT', 'Python', 'Node-RED', 'Industrial RPA', 'Siemens', 'Rockwell'],
        'n8n_workflow': {
            'trigger': 'IoT Webhook / Schedule',
            'nodes': ['IoT Hub', 'Data Processing', 'AI Model', 'Alerts', 'Dashboard', 'ERP'],
            'complexity': 'Very High',
            'estimated_hours': 48
        },
        'python_api': {
            'endpoints': ['/api/iot/', '/api/production/', '/api/maintenance/', '/api/quality/'],
            'libraries': ['FastAPI', 'TensorFlow', 'PyTorch', 'InfluxDB', 'MQTT', 'OPC-UA'],
            'ai_features': 'Predictive maintenance, quality detection, demand forecasting, anomaly detection'
        },
        'pricing_tier': 'Enterprise',
        'pricing': {'start': '$1999/mo', 'enterprise': 'Custom'}
    },
    {
        'id': 15,
        'name': 'Logistics & Supply Chain Automation',
        'slug': 'logistics-automation',
        'icon': '🚚',
        'color': '#0ea5e9',
        'description': 'Optimize routes, tracking, warehousing, and procurement with AI-powered automation.',
        'full_description': '''
            Logistics automation streamlines the entire supply chain from warehouse to delivery. 
            Use AI for route optimization, demand forecasting, and procurement automation to reduce 
            costs and improve delivery times.
        ''',
        'services': [
            'Route Optimization AI', 'Fleet Tracking Automation', 'Shipment Tracking Automation',
            'Demand Forecasting AI', 'Warehouse Automation', 'Procurement Automation',
            'Supplier Scoring AI', 'Dispatch Automation', 'Customs Documentation Automation', 'Logistics Analytics Automation'
        ],
        'use_cases': [
            'Route planning', 'Fleet management', 'Warehouse operations',
            'Demand forecasting', 'Supplier management', 'Customs processing'
        ],
        'tools': ['n8n', 'Zapier', 'Python', 'TensorFlow', 'ORT-Tools', 'ShipStation', 'EasyPost'],
        'n8n_workflow': {
            'trigger': 'Schedule / Webhook',
            'nodes': ['Schedule', 'Tracking API', 'AI Optimizer', 'Fleet System', 'Notifications'],
            'complexity': 'High',
            'estimated_hours': 28
        },
        'python_api': {
            'endpoints': ['/api/routes/', '/api/shipments/', '/api/suppliers/', '/api/forecasting/'],
            'libraries': ['FastAPI', 'TensorFlow', 'OR-Tools', 'Pandas', 'Google Maps API'],
            'ai_features': 'Route optimization, demand forecasting, supplier scoring'
        },
        'pricing_tier': 'Enterprise',
        'pricing': {'start': '$1299/mo', 'enterprise': 'Custom'}
    },
    {
        'id': 16,
        'name': 'Healthcare Automation',
        'slug': 'healthcare-automation',
        'icon': '🏥',
        'color': '#22c55e',
        'description': 'Automate patient scheduling, medical records, diagnostics, and healthcare operations.',
        'full_description': '''
            Healthcare automation improves patient care while reducing administrative burden. 
            From appointment scheduling to insurance claims processing, automate workflows while 
            maintaining HIPAA compliance and data security.
        ''',
        'services': [
            'Appointment Scheduling Automation', 'Patient Triage AI', 'Medical Transcription Automation',
            'EMR Automation', 'Diagnostic AI Workflows', 'Insurance Claim Automation',
            'Prescription Automation', 'Lab Report Automation', 'Remote Patient Monitoring', 'Healthcare Analytics Automation'
        ],
        'use_cases': [
            'Appointment booking', 'Patient triage', 'Medical coding',
            'Claims processing', 'Remote monitoring', 'Clinical notes'
        ],
        'tools': ['Epic', 'Cerner', 'n8n', 'Python', 'HL7 FHIR', 'Twilio', 'Zoom'],
        'n8n_workflow': {
            'trigger': 'Schedule / Webhook / HL7',
            'nodes': ['HL7/Webhook', 'AI Triage', 'EMR', 'Billing', 'Notifications'],
            'complexity': 'Very High',
            'estimated_hours': 40
        },
        'python_api': {
            'endpoints': ['/api/patients/', '/api/appointments/', '/api/claims/', '/api/diagnostics/'],
            'libraries': ['FastAPI', 'OpenAI', 'HL7', 'FHIR', 'Pydantic'],
            'ai_features': 'Patient triage, medical coding, claims automation, clinical NLP'
        },
        'pricing_tier': 'Enterprise',
        'pricing': {'start': '$1999/mo', 'enterprise': 'Custom'}
    },
    {
        'id': 17,
        'name': 'Banking & Fintech Automation',
        'slug': 'banking-automation',
        'icon': '🏦',
        'color': '#1e40af',
        'description': 'Automate KYC, lending, fraud detection, and compliance in financial services.',
        'full_description': '''
            Financial services automation handles sensitive transactions with security and compliance. 
            From KYC verification to fraud detection, build automated systems that reduce risk 
            while improving customer experience.
        ''',
        'services': [
            'KYC Automation', 'AML Automation', 'Risk Scoring AI',
            'Loan Processing Automation', 'Fraud Detection Automation', 'Transaction Monitoring',
            'Digital Banking Bots', 'Claims Automation', 'Credit Assessment Automation', 'Compliance Automation'
        ],
        'use_cases': [
            'Identity verification', 'Loan underwriting', 'Fraud detection',
            'Compliance reporting', 'Credit scoring', 'Transaction monitoring'
        ],
        'tools': ['Python', 'TensorFlow', 'n8n', 'RegTech APIs', 'Blockchain', 'Plaid', 'Stripe'],
        'n8n_workflow': {
            'trigger': 'Webhook / Schedule',
            'nodes': ['Webhook', 'KYC Service', 'Risk Model', 'Approval', 'Notifications', 'Audit'],
            'complexity': 'Very High',
            'estimated_hours': 48
        },
        'python_api': {
            'endpoints': ['/api/kyc/', '/api/loans/', '/api/fraud/', '/api/compliance/'],
            'libraries': ['FastAPI', 'TensorFlow', 'Cryptography', 'Pandas', 'Scikit-learn'],
            'ai_features': 'Fraud detection, credit scoring, risk assessment, AML monitoring'
        },
        'pricing_tier': 'Enterprise',
        'pricing': {'start': '$2499/mo', 'enterprise': 'Custom'}
    },
    {
        'id': 18,
        'name': 'Legal & Compliance Automation',
        'slug': 'legal-automation',
        'icon': '⚖️',
        'color': '#7c3aed',
        'description': 'Automate contract lifecycle, discovery, compliance monitoring, and case management.',
        'full_description': '''
            Legal automation streamlines contract management, discovery, and compliance. Use AI to 
            review contracts, automate compliance checks, and manage legal workflows efficiently 
            while reducing risk.
        ''',
        'services': [
            'Contract Lifecycle Automation', 'Legal Research Automation', 'E-discovery Automation',
            'Compliance Monitoring', 'Risk Assessment Automation', 'Policy Enforcement Automation',
            'Regulatory Reporting Automation', 'Litigation Analytics AI', 'IP Document Automation', 'Case Management Automation'
        ],
        'use_cases': [
            'Contract review', 'Compliance monitoring', 'E-discovery',
            'Legal research', 'Policy management', 'Case tracking'
        ],
        'tools': ['DocuSign CLM', 'Ironclad', 'n8n', 'Python', 'LangChain', ' Relativity'],
        'n8n_workflow': {
            'trigger': 'Webhook / Schedule',
            'nodes': ['Webhook', 'AI Contract Parser', 'Compliance Check', 'Approval', 'Alert'],
            'complexity': 'High',
            'estimated_hours': 32
        },
        'python_api': {
            'endpoints': ['/api/contracts/', '/api/compliance/', '/api/cases/', '/api/research/'],
            'libraries': ['FastAPI', 'LangChain', 'OpenAI', 'Pydantic'],
            'ai_features': 'Contract analysis, compliance checking, legal research, document extraction'
        },
        'pricing_tier': 'Enterprise',
        'pricing': {'start': '$1499/mo', 'enterprise': 'Custom'}
    },
    {
        'id': 19,
        'name': 'Education & EdTech Automation',
        'slug': 'education-automation',
        'icon': '🎓',
        'color': '#eab308',
        'description': 'Transform learning with AI tutors, grading automation, and personalized education.',
        'full_description': '''
            EdTech automation enhances learning experiences while reducing instructor workload. 
            From AI tutoring to automated grading, personalize education at scale with intelligent 
            automation.
        ''',
        'services': [
            'AI Tutor Bots', 'Content Generation Automation', 'Test Grading Automation',
            'Attendance Automation', 'Student Engagement Analytics', 'Admissions Automation',
            'Curriculum Recommendation AI', 'Plagiarism Detection Automation', 'Fee Management Automation', 'Learning Analytics Automation'
        ],
        'use_cases': [
            'AI tutoring', 'Automated grading', 'Personalized learning',
            'Attendance tracking', 'Admissions processing', 'Curriculum planning'
        ],
        'tools': ['Canvas', 'Moodle', 'Python', 'LangChain', 'Turnitin', 'Calendly'],
        'n8n_workflow': {
            'trigger': 'Webhook / Schedule',
            'nodes': ['LMS Webhook', 'AI Tutor', 'Grading', 'Analytics', 'Notifications'],
            'complexity': 'High',
            'estimated_hours': 28
        },
        'python_api': {
            'endpoints': ['/api/students/', '/api/courses/', '/api/grading/', '/api/analytics/'],
            'libraries': ['FastAPI', 'LangChain', 'OpenAI', 'Pandas'],
            'ai_features': 'AI tutoring, automatic grading, plagiarism detection, learning recommendations'
        },
        'pricing_tier': 'Mid-market',
        'pricing': {'start': '$499/mo', 'enterprise': 'Custom'}
    },
    {
        'id': 20,
        'name': 'Real Estate Automation',
        'slug': 'real-estate-automation',
        'icon': '🏠',
        'color': '#059669',
        'description': 'Automate property listings, lead management, and transaction workflows.',
        'full_description': '''
            Real estate automation streamlines property management from lead capture to closing. 
            Automate listings, tenant screening, maintenance requests, and more while providing 
            exceptional customer experiences.
        ''',
        'services': [
            'Property Listing Automation', 'Lead Qualification Bots', 'Property Recommendation AI',
            'Valuation Automation', 'Lease Management Automation', 'Maintenance Automation',
            'Rent Collection Automation', 'Market Trend Prediction', 'Chat-based Property Tours', 'CRM Automation'
        ],
        'use_cases': [
            'Lead capture', 'Property valuations', 'Tenant screening',
            'Lease management', 'Maintenance requests', 'Rent collection'
        ],
        'tools': ['Salesforce', 'HubSpot', 'Zapier', 'n8n', 'Zillow API', 'AppFolio', 'Buildium'],
        'n8n_workflow': {
            'trigger': 'Webhook / Schedule',
            'nodes': ['CRM Webhook', 'AI Lead Qualifier', 'Property Match', 'Calendar', 'Notifications'],
            'complexity': 'Medium',
            'estimated_hours': 20
        },
        'python_api': {
            'endpoints': ['/api/properties/', '/api/leads/', '/api/tenants/', '/api/valuations/'],
            'libraries': ['FastAPI', 'Scikit-learn', 'OpenAI', 'Zillow API'],
            'ai_features': 'Property valuation, lead scoring, recommendation engine, market analysis'
        },
        'pricing_tier': 'Mid-market',
        'pricing': {'start': '$399/mo', 'enterprise': 'Custom'}
    },
    {
        'id': 21,
        'name': 'Media & Creative Automation',
        'slug': 'media-automation',
        'icon': '🎬',
        'color': '#db2777',
        'description': 'Automate content creation, video editing, and creative workflows with AI.',
        'full_description': '''
            Media automation accelerates content production using AI. From automated video editing 
            to content repurposing, scale your creative operations while maintaining quality 
            and consistency.
        ''',
        'services': [
            'Content Generation AI', 'Video Editing Automation', 'Audio Transcription Automation',
            'Caption & Subtitle Automation', 'Thumbnail Automation', 'Publishing Automation',
            'Content Recommendation AI', 'Ad Placement Optimization', 'Copyright Detection AI', 'Influencer Analytics Automation'
        ],
        'use_cases': [
            'Video editing', 'Content creation', 'Subtitles',
            'Social publishing', 'Ad optimization', 'Influencer analysis'
        ],
        'tools': ['FFmpeg', 'Python', 'LangChain', 'Runway', 'Descript', 'YouTube API', '社交媒体 APIs'],
        'n8n_workflow': {
            'trigger': 'Schedule / Webhook',
            'nodes': ['Content Source', 'AI Generator', 'Video Editor', 'Thumbnail', 'Publish'],
            'complexity': 'High',
            'estimated_hours': 28
        },
        'python_api': {
            'endpoints': ['/api/content/', '/api/video/', '/api/media/', '/api/publishing/'],
            'libraries': ['FastAPI', 'OpenAI', 'FFmpeg', 'MoviePy', 'LangChain'],
            'ai_features': 'Content generation, video editing, transcription, thumbnails, SEO optimization'
        },
        'pricing_tier': 'Mid-market',
        'pricing': {'start': '$599/mo', 'enterprise': 'Custom'}
    },
    {
        'id': 22,
        'name': 'Government & Public Sector Automation',
        'slug': 'government-automation',
        'icon': '🏛️',
        'color': '#475569',
        'description': 'Modernize citizen services, document processing, and public sector operations.',
        'full_description': '''
            Government automation improves public services while reducing costs. From citizen portals 
            to permit processing, build secure, accessible automation that serves constituents 
            more effectively.
        ''',
        'services': [
            'Citizen Service Bots', 'Document Verification Automation', 'License Automation',
            'Public Grievance Automation', 'Tax Automation', 'Compliance Automation',
            'E-tender Automation', 'Identity Verification Automation', 'Policy Analytics Automation', 'Smart City Automation'
        ],
        'use_cases': [
            'Citizen support', 'Permit processing', 'Tax filing',
            'Identity verification', 'Tender management', 'Service requests'
        ],
        'tools': ['n8n', 'Zapier', 'Python', 'GovTech APIs', 'Blockstack', 'GOV.UK Notify'],
        'n8n_workflow': {
            'trigger': 'Portal Webhook / Schedule',
            'nodes': ['Portal Webhook', 'AI Agent', 'Document Verification', 'Approval', 'Citizen Portal'],
            'complexity': 'High',
            'estimated_hours': 36
        },
        'python_api': {
            'endpoints': ['/api/citizens/', '/api/permits/', '/api/services/', '/api/analytics/'],
            'libraries': ['FastAPI', 'Pydantic', 'Cryptography', 'OpenID Connect'],
            'ai_features': 'Document verification, citizen support bot, service recommendations'
        },
        'pricing_tier': 'Enterprise',
        'pricing': {'start': '$1999/mo', 'enterprise': 'Custom'}
    },
    {
        'id': 23,
        'name': 'Energy, Utilities & Environment Automation',
        'slug': 'energy-automation',
        'icon': '⚡',
        'color': '#fbbf24',
        'description': 'Optimize grid operations, energy consumption, and utility services with AI.',
        'full_description': '''
            Energy automation improves efficiency across power generation, distribution, and consumption. 
            Use AI for demand forecasting, grid optimization, and predictive maintenance to build 
            sustainable energy systems.
        ''',
        'services': [
            'Grid Optimization AI', 'Meter Reading Automation', 'Energy Forecasting AI',
            'Outage Management Automation', 'Maintenance Automation', 'Renewable Energy Analytics',
            'Asset Monitoring Automation', 'Carbon Tracking Automation', 'Utility Billing Automation', 'Field Workforce Automation'
        ],
        'use_cases': [
            'Grid balancing', 'Demand forecasting', 'Meter reading',
            'Outage response', 'Asset monitoring', 'Carbon tracking'
        ],
        'tools': ['AWS IoT', 'Azure IoT', 'Python', 'TensorFlow', 'SCADA', ' OSIsoft'],
        'n8n_workflow': {
            'trigger': 'IoT / Schedule',
            'nodes': ['IoT Hub', 'Energy Model', 'Grid Control', 'Alerts', 'Billing'],
            'complexity': 'Very High',
            'estimated_hours': 44
        },
        'python_api': {
            'endpoints': ['/api/energy/', '/api/meters/', '/api/assets/', '/api/forecasting/'],
            'libraries': ['FastAPI', 'TensorFlow', 'IoT Hub', 'InfluxDB', 'MQTT'],
            'ai_features': 'Demand forecasting, grid optimization, anomaly detection, predictive maintenance'
        },
        'pricing_tier': 'Enterprise',
        'pricing': {'start': '$2499/mo', 'enterprise': 'Custom'}
    },
    {
        'id': 24,
        'name': 'Agriculture & AgriTech Automation',
        'slug': 'agriculture-automation',
        'icon': '🌾',
        'color': '#65a30d',
        'description': 'Transform farming with AI-powered crop monitoring, irrigation, and supply chain.',
        'full_description': '''
            AgriTech automation brings precision agriculture to farming operations. Use IoT sensors, 
            drones, and AI to optimize irrigation, predict yields, and manage the entire agricultural 
            supply chain.
        ''',
        'services': [
            'Crop Yield Prediction', 'Irrigation Automation', 'Pest Detection AI',
            'Soil Analysis Automation', 'Farm Equipment Automation', 'Weather Advisory Automation',
            'Supply Chain Automation', 'Market Pricing AI', 'Farmer Advisory Bots', 'Agri-analytics Automation'
        ],
        'use_cases': [
            'Crop monitoring', 'Irrigation control', 'Pest detection',
            'Yield prediction', 'Market pricing', 'Equipment management'
        ],
        'tools': ['Python', 'TensorFlow', 'IoT sensors', 'NASA Earth Data', 'John Deere API', 'FarmBot'],
        'n8n_workflow': {
            'trigger': 'IoT / Schedule / Weather API',
            'nodes': ['Sensors', 'Weather', 'AI Model', 'Irrigation', 'Alerts', 'Analytics'],
            'complexity': 'High',
            'estimated_hours': 36
        },
        'python_api': {
            'endpoints': ['/api/crops/', '/api/sensors/', '/api/irrigation/', '/api/market/'],
            'libraries': ['FastAPI', 'TensorFlow', 'Pandas', 'OpenWeatherMap', 'NASA Power'],
            'ai_features': 'Yield prediction, pest detection, irrigation optimization, market forecasting'
        },
        'pricing_tier': 'Mid-market',
        'pricing': {'start': '$799/mo', 'enterprise': 'Custom'}
    },
    {
        'id': 25,
        'name': 'Security, Risk & Fraud Automation',
        'slug': 'security-fraud-automation',
        'icon': '🔒',
        'color': '#dc2626',
        'description': 'Protect your organization with AI-powered threat detection and access control.',
        'full_description': '''
            Security automation provides 24/7 protection against threats. From identity verification 
            to real-time threat detection, build defense systems that learn and adapt to emerging risks.
        ''',
        'services': [
            'Identity Verification AI', 'Access Control Automation', 'Fraud Detection Systems',
            'Threat Intelligence Automation', 'Surveillance Analytics AI', 'Risk Monitoring Automation',
            'Incident Response Automation', 'Compliance Auditing Automation', 'Credential Management Automation', 'Security Reporting Automation'
        ],
        'use_cases': [
            'Identity verification', 'Fraud prevention', 'Access control',
            'Threat monitoring', 'Incident response', 'Compliance audits'
        ],
        'tools': ['CrowdStrike', 'Splunk', 'Python', 'TensorFlow', 'SIEM tools', 'Okta', 'Azure AD'],
        'n8n_workflow': {
            'trigger': 'SIEM Webhook / Schedule',
            'nodes': ['Security Events', 'AI Detection', 'SOAR', 'Ticketing', 'Notifications'],
            'complexity': 'Very High',
            'estimated_hours': 48
        },
        'python_api': {
            'endpoints': ['/api/security/', '/api/identity/', '/api/threats/', '/api/compliance/'],
            'libraries': ['FastAPI', 'TensorFlow', 'Cryptography', 'Scapy', 'PySIEM'],
            'ai_features': 'Anomaly detection, fraud scoring, threat intelligence, behavioral analysis'
        },
        'pricing_tier': 'Enterprise',
        'pricing': {'start': '$1999/mo', 'enterprise': 'Custom'}
    },
    {
        'id': 26,
        'name': 'No-Code / Low-Code Automation Services',
        'slug': 'nocode-lowcode-automation',
        'icon': '🎨',
        'color': '#06b6d4',
        'description': 'Build automation workflows without coding using popular no-code platforms.',
        'full_description': '''
            No-code automation empowers business users to build integrations and workflows without 
            engineering support. Connect your favorite tools and automate processes in minutes, 
            not months.
        ''',
        'services': [
            'Zapier Workflow Automation', 'Make (Integromat) Automation', 'n8n Automation',
            'Power Automate Workflows', 'Airtable Automation', 'Notion Automation',
            'Bubble App Automation', 'Retool Dashboards', 'Voiceflow Bots', 'Form-to-CRM Automation'
        ],
        'use_cases': [
            'App integrations', 'Workflow automation', 'Dashboard building',
            'Internal tools', 'Form processing', 'Bot creation'
        ],
        'tools': ['Zapier', 'Make', 'n8n', 'Power Automate', 'Airtable', 'Notion', 'Bubble', 'Retool'],
        'n8n_workflow': {
            'trigger': 'Various (Webhooks, Schedules, App Events)',
            'nodes': ['Platform-specific nodes (5000+)'],
            'complexity': 'Low',
            'estimated_hours': 4
        },
        'python_api': None,
        'pricing_tier': 'All',
        'pricing': {'start': '$99/mo', 'enterprise': 'Custom'}
    },
    {
        'id': 27,
        'name': 'Full-Code / Custom Automation Services',
        'slug': 'fullcode-custom-automation',
        'icon': '💻',
        'color': '#8b5cf6',
        'description': 'Build bespoke AI agents, multi-agent systems, and custom automation solutions.',
        'full_description': '''
            Full-code automation provides complete flexibility for complex requirements. Build 
            custom AI agents, multi-agent systems, and enterprise integrations that go beyond 
            platform limitations.
        ''',
        'services': [
            'Custom AI Agents', 'Multi-agent AI Systems', 'LangChain Pipelines',
            'LLM Orchestration Systems', 'Custom RPA Scripting', 'API Orchestration Layers',
            'Event-driven Automation', 'Microservice Automation', 'Custom SaaS Automation', 'Enterprise Automation Platforms'
        ],
        'use_cases': [
            'Custom AI assistants', 'Complex workflows', 'Enterprise integrations',
            'Legacy system modernization', 'Real-time processing', 'Custom platforms'
        ],
        'tools': ['Python', 'LangChain', 'LlamaIndex', 'FastAPI', 'Docker', 'Kubernetes', 'AWS', 'GCP'],
        'n8n_workflow': {
            'trigger': 'Custom Webhook',
            'nodes': ['HTTP Request', 'Python Function', 'AI Agent', 'Custom Integration'],
            'complexity': 'Very High',
            'estimated_hours': 60
        },
        'python_api': {
            'endpoints': ['/api/agents/', '/api/workflows/', '/api/tasks/', '/api/llm/'],
            'libraries': ['FastAPI', 'LangChain', 'LlamaIndex', 'OpenAI', 'Anthropic', 'Pydantic', 'Docker', 'Kubernetes'],
            'ai_features': 'Custom AI agents, RAG systems, multi-agent orchestration, fine-tuned models'
        },
        'pricing_tier': 'Enterprise',
        'pricing': {'start': '$2999/mo', 'enterprise': 'Custom'}
    },
    {
        'id': 28,
        'name': 'AI Strategy & Automation Consulting',
        'slug': 'ai-strategy-consulting',
        'icon': '🎯',
        'color': '#f43f5e',
        'description': 'Strategic consulting for automation roadmap, ROI analysis, and AI implementation.',
        'full_description': '''
            AI Strategy consulting helps organizations navigate their automation journey. From 
            opportunity assessment to implementation planning, we help you build the right 
            automation strategy for your business.
        ''',
        'services': [
            'Automation Opportunity Assessment', 'ROI Analysis & Automation Roadmap', 'AI Architecture Design',
            'Tool Selection Consulting', 'Process Re-engineering', 'AI Governance Consulting',
            'Ethical AI Consulting', 'Scalability Planning', 'Automation Audits'
        ],
        'use_cases': [
            'Strategy planning', 'ROI analysis', 'Tool selection',
            'Process optimization', 'Governance frameworks', 'Capability building'
        ],
        'tools': ['Assessment frameworks', 'ROI calculators', 'Industry benchmarks', 'Workshops'],
        'n8n_workflow': None,
        'python_api': None,
        'pricing_tier': 'Consulting',
        'pricing': {'start': '$5000 (one-time)', 'enterprise': 'Custom'}
    },
]
