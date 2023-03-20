import pytest

from task_28 import sub_idx


@pytest.mark.parametrize("haystack, needle, ans", [
    ("sadbutsad", "sad", 0),
    ("leetcode", "leeto", -1),
])
def test_examples(haystack, needle, ans):
    return sub_idx(haystack, needle) == ans
