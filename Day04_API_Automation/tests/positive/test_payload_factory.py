from Day04_API_Automation.framework.payloads.notebook_payload import (
    create_notebook_payload
)


def test_payload_factory():

    payload1 = create_notebook_payload()
    payload2 = create_notebook_payload()

    assert payload1["title"]
    assert payload2["title"]

    assert payload1["title"] != payload2["title"]

    assert payload1["description"]
    assert payload2["description"]