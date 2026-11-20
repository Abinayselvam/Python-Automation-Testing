import pytest


@pytest.mark.skip(reason="Feature is not implemented")
def test_payment():
    assert True


@pytest.mark.skipif(
    2 < 3,
    reason="Condition is true, so skip this test"
)
def test_skip_condition():
    assert True


@pytest.mark.xfail(reason="Known bug - waiting for a fix")
def test_known_bug():
    assert 10 == 20


def test_normal_case():
    assert 5 == 5