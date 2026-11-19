from playwright.sync_api import (
    sync_playwright,
    TimeoutError as PlaywrightTimeoutError
)

with sync_playwright() as playwright:

    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()

    try:
        page.goto("https://example.com")

        page.get_by_role(
            "button",
            name="Login"
        ).click(timeout=3000)

    except PlaywrightTimeoutError:
        print("Login button was not available within 3 seconds")

    finally:
        browser.close()