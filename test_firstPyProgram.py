import pytest


@pytest.mark.usefixtures("conft")
class TestExample:


    def test_fixtureDemo(self):
        print("i will execute steps in fixtureDemo method")


    def test_fixtureDemo1(self):
        print("i will execute steps in fixtureDemo1 method")


    def test_fixtureDemo2(self):
        print("i will execute steps in fixtureDemo2 method")


    def test_fixtureDemo3(self):
        print("i will execute steps in fixtureDemo3 method")


    def test_fixtureDemo4(self):
        print("i will execute steps in fixtureDemo4 method")
        
    def test_fixtureDemo5(self):
        print("i will execute steps in fixtureDemo5 method")    