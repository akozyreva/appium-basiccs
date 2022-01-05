import pytest

# module setup-teardown
# see https://docs.pytest.org/en/6.2.x/xunit_setup.html


def setup_module():
    print("Creating db connection")


def teardown_module():
    print("Closing db connection")

# scope is this file only


def setup_function():
    # it's the same as usual fixture, but it's written in unittest way
    print("Browser is launching")


def teardown_function():
    print("Browser is closing")


def test_do_login():
    print("Executing login test")
    assert True


def test_user_registration():
    print("Executing registration test")
    assert True