import pytest

def test_not_equal(my_rectangle,wierd_rectangle):
    assert my_rectangle != wierd_rectangle

def test_area(my_rectangle):
    assert my_rectangle.area() == 10 * 20

def test_perimeter(my_rectangle):
    assert my_rectangle.perimeter() == (10 * 2) + (20 * 2)