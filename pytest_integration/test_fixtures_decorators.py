import pytest


@pytest.fixture(scope="module", autouse=True)
def setup():
    print("Creating db connection...")
    yield
    print("Closing db connection")


@pytest.fixture(scope="function")
def before():
    print("Launching browser")
    yield
    print("Closing browser")


def test_do_logout(before):
    print("Executing logout test")
    assert True

# you can use decorator - it's more clearable, then to pass it to parameter !!!


@pytest.mark.usefixtures("before")
def test_user_fail_registration():
    print("Executing registration fail test")
    assert True