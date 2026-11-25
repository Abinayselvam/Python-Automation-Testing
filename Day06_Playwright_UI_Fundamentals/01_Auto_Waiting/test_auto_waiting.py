from playwright.sync_api import Page, expect


def test_login_button(page: Page):

    page.goto("https://www.saucedemo.com/")

    username = page.get_by_placeholder(
        "Username"
    )

    password = page.get_by_placeholder(
        "Password"
    )

    login_button = page.get_by_role(
        "button",
        name="Login"
    )

    username.fill("standard_user")
    password.fill("secret_sauce")

    login_button.click()

    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )