from playwright.sync_api import sync_playwright


def test_teacher_student_context():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)

        # Create independent sessions
        teacher_context = browser.new_context()
        student_context = browser.new_context()

        # Create separate pages
        teacher_page = teacher_context.new_page()
        student_page = student_context.new_page()

        teacher_page.goto("https://example.com")
        student_page.goto("https://example.com")

        # Set different local storage values
        teacher_page.evaluate(
            "() => localStorage.setItem('role', 'Teacher')"
        )

        student_page.evaluate(
            "() => localStorage.setItem('role', 'Student')"
        )

        # Validate session isolation
        teacher_role = teacher_page.evaluate(
            "() => localStorage.getItem('role')"
        )

        student_role = student_page.evaluate(
            "() => localStorage.getItem('role')"
        )

        assert teacher_role == "Teacher"
        assert student_role == "Student"

        # Clean up
        teacher_context.close()
        student_context.close()
        browser.close()