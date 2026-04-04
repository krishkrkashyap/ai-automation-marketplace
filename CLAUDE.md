# AI Automation Marketplace - Project Documentation

## Overview
Django + HTMX + Tailwind CSS website with 28 automation service categories. Each category includes n8n workflow templates and Python/FastAPI services for AI-powered automations.

## Running the Project

### Start Django Server
```bash
cd C:/Users/krish/ai-automation-marketplace
python manage.py runserver 8080
```

### Start FastAPI Service
```bash
cd C:/Users/krish/ai-automation-marketplace/api-services
uvicorn main:app --host 0.0.0.0 --port 8000
```

### n8n Cloud
- URL: https://krishkrkashya.app.n8n.cloud
- API key configured in environment

## 28 Automation Categories

1. business-process-automation
2. robotic-process-automation
3. ai-chatbot-automation
4. sales-automation
5. marketing-automation
6. customer-support-automation
7. finance-automation
8. hr-automation
9. it-devops-automation
10. data-automation
11. ai-ml-automation
12. document-automation
13. ecommerce-automation
14. manufacturing-automation
15. logistics-automation
16. healthcare-automation
17. banking-automation
18. legal-automation
19. education-automation
20. real-estate-automation
21. media-automation
22. government-automation
23. energy-automation
24. agriculture-automation
25. security-fraud-automation
26. nocode-lowcode-automation
27. fullcode-custom-automation
28. ai-strategy-consulting

## Key Files

- `pages/automations_data.py` - 28 automation categories data
- `pages/n8n_integration.py` - N8N workflow manager
- `pages/api_views.py` - Django API endpoints
- `api-services/main.py` - FastAPI with 28 endpoints
- `n8n-workflows/` - 28 JSON workflow files
- `templates/pages/automation_detail.html` - Detail page with Execute button
- `test_all_workflows.py` - Playwright browser test script
- `test_screenshots/` - 56 screenshots (before/after each test)
- `test_results.json` - Test results (28/28 passed)

## Testing

Run browser automation test:
```bash
python test_all_workflows.py
```

All 28 workflows tested successfully with Playwright browser automation.
