import re
from playwright.sync_api import Page, expect


def test_case_insensitive_text(page: Page):

    page.set_content("""
        <h1>WELCOME TEACHER</h1>
        <p>Student Dashboard</p>
    """)

    search_text = "welcome teacher"

    pattern = re.compile(
        search_text,
        re.I
    )

    heading = page.get_by_text(pattern)

    expect(heading).to_be_visible()