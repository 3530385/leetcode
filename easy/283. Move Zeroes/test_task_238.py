import pytest
from task_238 import move_zeroes


@pytest.mark.parametrize("nums, results", [
    ([1, 0, 2, 0, 4, 0], [1, 2, 4, 0, 0, 0]),
    ([0],  [0]),
    ([0, 0, 0, 0, 0], [0, 0, 0, 0, 0]),
    ])
def test_task(nums: list, results: list):
    move_zeroes(nums)
    assert nums == results
