
import pytest
from roman_converter.utils import roman_to_arabic, arabic_to_roman

# Test cases for roman_to_arabic function
def test_roman_to_arabic_basic():
    assert roman_to_arabic("III") == 3
    assert roman_to_arabic("IV") == 4
    assert roman_to_arabic("IX") == 9
    assert roman_to_arabic("LVIII") == 58
    assert roman_to_arabic("MCMXCIV") == 1994

def test_roman_to_arabic_invalid_input():
    with pytest.raises(SystemExit):
        roman_to_arabic("INVALID")

# Test cases for arabic_to_roman function
def test_arabic_to_roman_basic():
    assert arabic_to_roman(3) == "III"
    assert arabic_to_roman(4) == "IV"
    assert arabic_to_roman(9) == "IX"
    assert arabic_to_roman(58) == "LVIII"
    assert arabic_to_roman(1994) == "MCMXCIV"

def test_arabic_to_roman_invalid_input():
    with pytest.raises(SystemExit):
        arabic_to_roman(0)
    with pytest.raises(SystemExit):
        arabic_to_roman(4000)

if __name__ == '__main__':
    pytest.main()