import pytest

from task_58 import *


@pytest.mark.parametrize("string, ans", [
    ("Hello World", 5),
    ("   fly me   to   the moon  ", 4),
    ("   fly me   to   the moon  ", 4),
    ("luffy is still joyboy", 6),
    ("s", 1),
    ("s         ", 1),
])
def test_examples(string, ans):
    assert length_of_last_world(string) == ans
    assert length_of_last_world_with_pop(string) == ans
    assert length_of_last_world_backprop(string) == ans
