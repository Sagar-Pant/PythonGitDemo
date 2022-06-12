import pytest


@pytest.mark.usefixtures("conft")
@pytest.mark.med
def test_t1Module():
    print("Yo bro")


@pytest.mark.usefixtures("conft")
@pytest.mark.medical
def test_t2Module():
    print("Mere a new more Module!!!")
