from playwright.sync_api import sync_playwright
import sys

BASE_URL = "http://localhost:8000"

PAGES_TO_TEST = [
    ("/", "Homepage"),
    ("/industries/", "Industries List"),
    ("/industries/ecommerce-automation/", "E-Commerce Industry"),
    ("/industries/finance-automation/", "Finance Industry"),
    ("/industries/healthcare-automation/", "Healthcare Industry"),
    ("/services/", "Services List"),
    ("/services/bots/lead-qualification-bot/", "Lead Qualification Bot"),
    ("/services/bots/invoice-processing-bot/", "Invoice Processing Bot"),
    ("/services/bots/customer-support-bot/", "Customer Support Bot"),
    ("/pricing/", "Pricing"),
    ("/contact/", "Contact"),
    ("/case-studies/", "Case Studies"),
    ("/blog/", "Blog"),
    ("/search/", "Search"),
    ("/sitemap.xml", "Sitemap"),
    ("/robots.txt", "Robots.txt"),
]

def test_pages():
    errors = []
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        for path, name in PAGES_TO_TEST:
            url = BASE_URL + path
            print(f"Testing: {name} ({url})")
            try:
                response = page.goto(url, wait_until="domcontentloaded", timeout=10000)
                if response and response.status == 200:
                    print(f"  [OK] {name} - Status 200")
                else:
                    print(f"  [FAIL] {name} - Status: {response.status if response else 'No response'}")
                    errors.append(f"{name}: Status {response.status if response else 'No response'}")
            except Exception as e:
                print(f"  [FAIL] {name} - Error: {str(e)[:50]}")
                errors.append(f"{name}: {str(e)[:50]}")
        
        browser.close()
    
    print("\n" + "="*50)
    if errors:
        print(f"FAILED: {len(errors)} page(s) with errors")
        for err in errors:
            print(f"  - {err}")
        return False
    else:
        print(f"SUCCESS: All {len(PAGES_TO_TEST)} pages loaded correctly!")
        return True

if __name__ == "__main__":
    success = test_pages()
    sys.exit(0 if success else 1)
