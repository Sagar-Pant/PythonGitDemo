import pytest


@pytest.mark.usefixtures("conft")
@pytest.mark.med
def test_t1Module():
    print("Yo bro")
