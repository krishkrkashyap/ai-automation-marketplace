import json
import time
from playwright.sync_api import sync_playwright

BASE_URL = "http://localhost:8080"

SERVICE_SLUGS = [
    'business-process-automation', 'robotic-process-automation', 'ai-chatbot-automation',
    'sales-automation', 'marketing-automation', 'customer-support-automation', 'finance-automation',
    'hr-automation', 'it-devops-automation', 'data-automation', 'ai-ml-automation',
    'document-automation', 'ecommerce-automation', 'manufacturing-automation', 'logistics-automation',
    'healthcare-automation', 'banking-automation', 'legal-automation', 'education-automation',
    'real-estate-automation', 'media-automation', 'government-automation', 'energy-automation',
    'agriculture-automation', 'security-fraud-automation', 'nocode-lowcode-automation',
    'fullcode-custom-automation', 'ai-strategy-consulting'
]

INDUSTRY_SLUGS = [
    'ecommerce-automation', 'finance-automation', 'healthcare-automation', 'education-automation',
    'real-estate-automation', 'marketing-automation', 'hr-automation', 'legal-automation',
    'manufacturing-automation', 'logistics-supply-chain-automation', 'banking-fintech-automation',
    'energy-utilities-automation', 'travel-automation', 'media-creative-automation', 'government-automation',
    'agriculture-automation', 'security-automation', 'automotive-automation', 'retail-automation',
    'insurance-automation', 'pharmaceutical-automation', 'construction-automation', 'telecommunications-automation',
    'food-beverage-automation', 'non-profit-automation', 'sports-automation', 'entertainment-automation',
    'transportation-automation'
]

OTHER_PAGES = [
    ('/', 'Home'),
    ('/services/', 'Services List'),
    ('/services/bots/', 'Bots List'),
    ('/industries/', 'Industries List'),
    ('/automations/', 'Automations List'),
    ('/pricing/', 'Pricing'),
    ('/contact/', 'Contact'),
    ('/case-studies/', 'Case Studies'),
]

def test_page(page, url, name):
    """Test a single page"""
    try:
        page.goto(url, timeout=15000)
        page.wait_for_load_state('networkidle')
        
        content = page.content()
        
        if '404' in page.title().lower() or 'not found' in content.lower()[:500]:
            return {'url': url, 'name': name, 'status': '404', 'has_execute': False}
        
        has_execute = 'Execute Workflow' in content
        
        return {'url': url, 'name': name, 'status': 'OK', 'has_execute': has_execute}
    except Exception as e:
        return {'url': url, 'name': name, 'status': f'ERROR: {str(e)[:50]}', 'has_execute': False}

def main():
    print("Testing all website pages with Playwright...")
    print(f"Base URL: {BASE_URL}")
    
    results = []
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(viewport={'width': 1920, 'height': 1080})
        page = context.new_page()
        
        print("\n=== Testing Other Pages ===")
        for path, name in OTHER_PAGES:
            url = BASE_URL + path
            print(f"Testing: {name} ({path})")
            result = test_page(page, url, name)
            results.append(result)
            print(f"  Status: {result['status']}")
            time.sleep(0.5)
        
        print("\n=== Testing Service Pages ===")
        for i, slug in enumerate(SERVICE_SLUGS, 1):
            url = f"{BASE_URL}/services/{slug}/"
            name = f"Service: {slug}"
            print(f"Testing ({i}/28): {slug}")
            result = test_page(page, url, name)
            results.append(result)
            if not result['status'].startswith('OK'):
                print(f"  ERROR: {result['status']}")
            time.sleep(0.5)
        
        print("\n=== Testing Industry Pages ===")
        for i, slug in enumerate(INDUSTRY_SLUGS, 1):
            url = f"{BASE_URL}/industries/{slug}/"
            name = f"Industry: {slug}"
            print(f"Testing ({i}/28): {slug}")
            result = test_page(page, url, name)
            results.append(result)
            if not result['status'].startswith('OK'):
                print(f"  ERROR: {result['status']}")
            time.sleep(0.5)
        
        browser.close()
    
    # Summary
    print("\n" + "="*60)
    print("TEST SUMMARY")
    print("="*60)
    
    ok_count = sum(1 for r in results if r['status'].startswith('OK'))
    error_count = sum(1 for r in results if not r['status'].startswith('OK'))
    execute_count = sum(1 for r in results if r['has_execute'])
    
    print(f"Total pages tested: {len(results)}")
    print(f"OK: {ok_count}")
    print(f"Errors: {error_count}")
    print(f"Pages with Execute Workflow: {execute_count}")
    
    errors = [r for r in results if not r['status'].startswith('OK')]
    if errors:
        print("\nPages with errors:")
        for r in errors:
            print(f"  - {r['name']}: {r['status']}")
    
    with open("C:/Users/krish/ai-automation-marketplace/test_results.json", "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to test_results.json")

if __name__ == "__main__":
    main()
