import pytest

from task_643 import find_max_subarray


# @pytest.mark.patametrize("num, k, result", [
#     ([1, 12, -5, -6, 50, 3], 4, 12.75),
#     ([0], 1, 0),
# ])
def test_f():
    assert find_max_subarray([1, 12, -5, -6, 50, 3], 4) == 12.75
    assert find_max_subarray([0],1) == 0