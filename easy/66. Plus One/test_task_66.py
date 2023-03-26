import pytest

from task_66 import plus_one


@pytest.mark.parametrize("digits, ans", [
    ([1, 2, 3], [1, 2, 4]),
    ([4, 3, 2, 1], [4, 3, 2, 2]),
    ([9], [1, 0]),
    ([9, 9, 9, 9], [1, 0, 0, 0, 0]),
    ([9, 9, 8, 9], [9, 9, 9, 0]),
])
def test_example(digits, ans):
    assert plus_one(digits) == ans
