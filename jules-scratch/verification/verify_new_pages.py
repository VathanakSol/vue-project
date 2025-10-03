from playwright.sync_api import Page, expect

def test_new_pages_navigation(page: Page):
    """
    This test verifies that the new 'Services' and 'Portfolio' pages
    are accessible from the navigation bar.
    """
    # 1. Arrange: Go to the homepage.
    # Assuming the dev server is running on the default Vite port 5173.
    page.goto("http://localhost:5173")

    # 2. Act: Click the "Services" link.
    services_link = page.get_by_role("link", name="Services")
    services_link.click()

    # 3. Assert: Check if the Services page is loaded.
    expect(page.get_by_role("heading", name="Services")).to_be_visible()
    expect(page.get_by_text("This is the services page.")).to_be_visible()

    # 4. Act: Click the "Portfolio" link.
    portfolio_link = page.get_by_role("link", name="Portfolio")
    portfolio_link.click()

    # 5. Assert: Check if the Portfolio page is loaded.
    expect(page.get_by_role("heading", name="Portfolio")).to_be_visible()
    expect(page.get_by_text("This is the portfolio page.")).to_be_visible()

    # 6. Act: Click the "Home" link to go back.
    home_link = page.get_by_role("link", name="Home")
    home_link.click()

    # 7. Assert: Check if the Home page is loaded and take a screenshot.
    expect(page.get_by_role("heading", name="This is Home Page")).to_be_visible()
    page.screenshot(path="jules-scratch/verification/verification.png")

# To run this script, you need to have playwright installed and browsers downloaded.
# pip install playwright
# playwright install
# Then run the script with pytest or by wrapping the function call.
# This is a simplified example. A full script would use a test runner.

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    test_new_pages_navigation(page)
    browser.close()