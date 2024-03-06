import pytest
import source.my_functions as my_functions
import time

def test_add():
    result=my_functions.add(1,2)
    assert result==3

def test_divide():
    result=my_functions.divide(10,5)
    assert result==2

def test_divide_by_zero():
    with pytest.raises(ValueError):
        my_functions.divide(10,0)

@pytest.mark.slow
def test_very_slow():
    time.sleep(5)
    result=my_functions.divide(10,5)
    assert result==2


# The below test will be skipped
@pytest.mark.skip(reason="This feature is currently broken")
def test_add():
    assert my_functions.add(1,2) == 3

@pytest.mark.xfail(reason="We know we cannot divide by zero")
def test_divide_zero_broken():
    my_functions.divide(4,0)

def test_add_strings():
    result=my_functions.add("I like ","Pizza")
    assert result=="I like Pizza"



