import pytest


@pytest.fixture(scope="class")
def conft():
    print("I will be executed first!!!")
    yield
    print("I will be executed last!!!")
