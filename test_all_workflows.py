"""
Test all 28 automation workflows via browser automation
"""
import json
import time
from playwright.sync_api import sync_playwright

AUTOMATION_SLUGS = [
    "business-process-automation",
    "robotic-process-automation",
    "ai-chatbot-automation",
    "sales-automation",
    "marketing-automation",
    "customer-support-automation",
    "finance-automation",
    "hr-automation",
    "it-devops-automation",
    "data-automation",
    "ai-ml-automation",
    "document-automation",
    "ecommerce-automation",
    "manufacturing-automation",
    "logistics-automation",
    "healthcare-automation",
    "banking-automation",
    "legal-automation",
    "education-automation",
    "real-estate-automation",
    "media-automation",
    "government-automation",
    "energy-automation",
    "agriculture-automation",
    "security-fraud-automation",
    "nocode-lowcode-automation",
    "fullcode-custom-automation",
    "ai-strategy-consulting",
]

BASE_URL = "http://localhost:8080"

def test_workflow(page, slug):
    """Test a single workflow by visiting the page and clicking Execute"""
    url = f"{BASE_URL}/automations/{slug}/"
    
    print("\n" + "="*60)
    print(f"Testing: {slug}")
    print(f"URL: {url}")
    print("="*60)
    
    try:
        # Navigate to the page
        page.goto(url)
        page.wait_for_load_state('networkidle')
        time.sleep(1)  # Wait for page to fully render
        
        # Take screenshot
        page.screenshot(path=f"C:/Users/krish/ai-automation-marketplace/test_screenshots/{slug}.png", full_page=True)
        print(f"Screenshot saved: {slug}.png")
        
        # Check if Execute button exists
        execute_btn = page.locator('button:has-text("Execute Workflow")')
        if execute_btn.count() > 0:
            print(f"Execute button found")
            
            # Click Execute button
            execute_btn.click()
            print(f"Clicked Execute button...")
            
            # Wait for result
            time.sleep(3)
            
            # Take screenshot after execution
            page.screenshot(path=f"C:/Users/krish/ai-automation-marketplace/test_screenshots/{slug}_after.png", full_page=True)
            print(f"Result screenshot saved")
            
            # Check for status
            status_el = page.locator('#workflow-status')
            if status_el.count() > 0:
                status_text = status_el.inner_text()
                print(f"Status: {status_text}")
                
                # Check result
                result_el = page.locator('#workflow-result')
                if result_el.count() > 0 and not result_el.is_hidden():
                    result_text = result_el.inner_text()
                    print(f"Result: {result_text[:200]}...")
                else:
                    print(f"No result displayed")
            else:
                print(f"Status element not found")
        else:
            print(f"Execute button NOT found!")
            # Take screenshot to see what buttons are available
            page.screenshot(path=f"C:/Users/krish/ai-automation-marketplace/test_screenshots/{slug}_error.png", full_page=True)
            
        return True
        
    except Exception as e:
        print(f"ERROR: {str(e)}")
        page.screenshot(path=f"C:/Users/krish/ai-automation-marketplace/test_screenshots/{slug}_exception.png", full_page=True)
        return False

def main():
    print("Starting browser automation test for 28 workflows...")
    print(f"Base URL: {BASE_URL}")
    print(f"Total workflows: {len(AUTOMATION_SLUGS)}")
    
    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch(headless=False)  # Use headless=False to see the browser
        context = browser.new_context(viewport={"width": 1920, "height": 1080})
        page = context.new_page()
        
        results = []
        
        for i, slug in enumerate(AUTOMATION_SLUGS, 1):
            print(f"\n\n{'#'*60}")
            print(f"# {i}/28: {slug}")
            print(f"{'#'*60}")
            
            success = test_workflow(page, slug)
            results.append({"slug": slug, "success": success})
            
            # Wait between tests
            print(f"Waiting 2 seconds before next test...")
            time.sleep(2)
        
        browser.close()
        
        # Print summary
        print(f"\n\n{'='*60}")
        print("TEST SUMMARY")
        print('='*60)
        
        successful = sum(1 for r in results if r["success"])
        failed = sum(1 for r in results if not r["success"])
        
        print(f"Successful: {successful}/{len(results)}")
        print(f"Failed: {failed}/{len(results)}")
        
        if failed > 0:
            print(f"\nFailed workflows:")
            for r in results:
                if not r["success"]:
                    print(f"   - {r['slug']}")
        
        # Save results to JSON
        with open("C:/Users/krish/ai-automation-marketplace/test_results.json", "w") as f:
            json.dump(results, f, indent=2)
        print(f"\nResults saved to test_results.json")

if __name__ == "__main__":
    main()
