import pytest

#define function to print input value
def show_input_value(n):
    if not isinstance(n,int):
        raise TypeError("input has to be integer")
    else:
        return n

# Test for valid input
def test_valid_input():
    with pytest.raises(TypeError):
        show_input_value("not an integer")

#Define function to compute square
def square(n):
    if not isinstance(n,int):
        raise TypeError("input has to be integer")
    else:
        return n ** 2

#Define function to compute cube
def cube(n):
    if not isinstance(n,int):
        raise TypeError("input has to be integer")
    else:
        return n ** 3

#Define function to compute fifth power
def fifth(n):
    if not isinstance(n,int):
        raise TypeError("input has to be integer")
    else:
        return n ** 5

#Test square function
def test_square():
    assert square(2) == 4, "Test failed, square of 2 should be 4"
    assert square(3) == 9, "Test failed, square of 3 should be 9"

#Test cube function
def test_cube():
    assert cube(2) == 8, "Test failed, cube of 2 should be 8"
    assert cube(3) == 27, "Test failed, cube of 3 should be 27"

#Test fifth power function
def test_fifth():
    assert fifth(2) == 32, "Test failed, fifth power of 2 should be 32"
    assert fifth(3) == 243, "Test failed, fifth power of 3 should be 243"



