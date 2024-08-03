import pytest
import divide

def test_divide_numbers_raises_valueerror():
    with pytest.raises(ValueError):
        divide.divide_numbers(10, 0)
    
# This code block is executed when this script is run directly
