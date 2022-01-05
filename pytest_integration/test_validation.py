import pytest_check as check


def test_validate_titles():
    expected_title = "Google.com"
    actual_title = "Gamil.com"
    assert expected_title == actual_title, f"Titles are not equal. " \
                                           f"Expected title {expected_title}, but actual is {actual_title}"


# how to get multiple failures of the test
# and continue to run tests
def test_verify_word_in_title():
    title = "This is Gmail website"
    check.is_in("Gmails", title, "Gmail is not in title")
    check.is_true(False)