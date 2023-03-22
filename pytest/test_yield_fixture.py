import pytest

@pytest.yield_fixture()#function name must be setup
def setup():#its like setup method in unit testing...excutes every time before and after completes the every function
    print('before yield')
    yield
    print('after yield')

def test_demo1(setup):
    print("test demo 1")

def test_demo2(setup):
    print('test demo 2')