class BasePage:

    def __init__(self, page):
        self.page = page

    def navigate(self, url):
        self.page.goto(url)

    def get_title(self):
        return self.page.title()

    def get_current_url(self):
        return self.page.current_url

    def close(self):
        self.page.close()