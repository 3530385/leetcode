import pytest

from main import is_palindrome


@pytest.mark.parametrize("x, answer", [
    (121, True),
    (-121, False),
    (10, False),
])
def test_examples(x, answer):
    assert is_palindrome(x) == answer
