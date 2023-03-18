import pytest

from main import is_valid


@pytest.mark.parametrize("s, answer", [
    ("()", True),
    ("()[]{}", True),
    ("(]", False),
    ("([)]", False),
    ("([((()))])", True),
])
def test_examples(s, answer):
    assert is_valid(s) == answer




