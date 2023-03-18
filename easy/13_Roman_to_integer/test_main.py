import pytest

from main import roman_to_int


@pytest.mark.parametrize("s, answer", [
    ("III", 3),
    ("LVIII", 58),
    ("MCMXCIV", 1994),
])
def test_roman_to_int(s, answer):
    assert roman_to_int(s) == answer

def test_speed():
    s = ""
