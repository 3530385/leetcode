from collections import Counter

import pytest

from task_27 import remove_element


@pytest.mark.parametrize("nums, val", [
    ([3, 2, 2, 3], 3),
    ([0, 1, 2, 2, 3, 0, 4, 2], 2),
])
def test_examples(nums, val):
    old_nums = nums.copy()
    cnt = Counter(old_nums)
    cnt.pop(val)
    assert remove_element(nums, val) == sum(cnt.values())
