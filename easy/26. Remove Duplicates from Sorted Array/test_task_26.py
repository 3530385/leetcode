import pytest

from task_26 import remove_duplicates


@pytest.mark.parametrize("nums", [
    ([1, 1, 2, 3, 4, 4, 5, 5, 6]),
    ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]),
    ([1, 1, 2]),
    ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]),
])
def test_example(nums):
    set_nums = set(nums)
    k = len(set_nums)
    assert k == remove_duplicates(nums)
    assert list(set_nums) == nums[:k]
