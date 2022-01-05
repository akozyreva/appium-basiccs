import pytest


def get_data():
    return [
        ("trainer@com", "123245"),
        ("akafd@com", "432432")
    ]


# "username, password" -> it's id to show in test
# it should be matched to variables in the test
@pytest.mark.parametrize("username, password", get_data())
def test_sign_up(username, password):
    print(username, password)