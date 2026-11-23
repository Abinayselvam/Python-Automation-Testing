02.api_fixtures
What happens?
1. Pytest starts the session.
2. Playwright creates an API request context.
3. Tests receive the fixture by its name.
4. Tests send API requests through the context.
5. At the end of the test session, dispose() releases the context.