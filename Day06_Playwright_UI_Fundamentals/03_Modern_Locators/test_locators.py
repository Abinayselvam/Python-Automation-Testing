from playwright.sync_api import Page, expect


def test_modern_locators(page: Page):

    page.goto("https://www.saucedemo.com/")

    # Placeholder locator
    username = page.get_by_placeholder("Username")

    # Test ID locator
    password = page.get_by_test_id("password")

    # Role locator
    login_button = page.get_by_role(
        "button",
        name="Login"
    )

    username.fill("standard_user")
    password.fill("secret_sauce")

    expect(login_button).to_be_visible()

    login_button.click()

    # Text locator
    expect(
        page.get_by_text("Products")
    ).to_be_visible()