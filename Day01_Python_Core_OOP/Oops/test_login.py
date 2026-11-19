from .login_page import LoginPage

# Mock browser page
class MockPage:

    def __init__(self):
        self.current_url = ""
        self.fields = {}

    def goto(self, url):
        self.current_url = url
        print(f"Navigated to: {url}")

    def title(self):
        return "Demo Login Page"

    def fill(self, locator, value):
        self.fields[locator] = value
        print(f"Entered {locator}: {value}")

    def click(self, locator):
        print(f"Clicked button: {locator}")

    def close(self):
        print("Browser page closed")


# Create mock page object
mock_page = MockPage()

# Create LoginPage object
login_page = LoginPage(mock_page)

# Execute page operations
login_page.navigate("https://example.com/login")

print("Page title:", login_page.get_title())

login_page.login("admin", "admin123")

print("Current URL:", login_page.get_current_url())

login_page.close()