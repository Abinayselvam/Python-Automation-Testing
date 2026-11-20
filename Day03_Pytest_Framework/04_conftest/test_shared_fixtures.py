def test_user_details(sample_user):
    assert sample_user["username"] == "admin"


def test_application_url(application_url):
    assert application_url.startswith("https://")