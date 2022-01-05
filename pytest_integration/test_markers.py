import pytest


@pytest.mark.functional
def test_search_product():
    print("Searching for product..")


@pytest.mark.regression
def test_order_product():
    print("Order product..")


def test_submit_email():
    print("Submit emailpy")