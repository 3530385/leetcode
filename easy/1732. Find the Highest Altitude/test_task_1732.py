import pytest

from task_1732 import largest_altitude


@pytest.mark.parametrize("gain, result", [
    ([-5, 1, 5, 0, -7], 1),
    ([-4, -3, -2, -1, 4, 3, 2], 0),
    ])
def test_largest_altitude(gain, result):
    assert largest_altitude(gain) == result
