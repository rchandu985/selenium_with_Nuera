import pytest

@pytest.fixture()#function name must be setup
def setup():#its like setup method in unit testing...excutes every time before excutes the function
    print('im setup')

def test_demo1(setup):
    print("test demo 1")

def test_demo2(setup):
    print('test demo 2')