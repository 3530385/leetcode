import pytest
from task_35 import search_insert


@pytest.mark.parametrize("nums, target, ans", [
    ([1, 3, 5, 6], 5, 2),
    ([1, 3, 5, 6], 2, 1),
    ([1, 3, 5, 6], 7, 4),
])
def test_examples(nums: list[int], target: int, ans: int) -> None:
    assert search_insert(nums, target) == ans
