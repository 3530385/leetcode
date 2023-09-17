import pytest
from main import one_line_solution


@pytest.mark.parametrize("word1, word2, result", [
    ("word1", "word2", "wwoorrdd12"),
    ("qwertyu", "cv", "qcwvertyu"),
    ])
def test_main(word1, word2, result):
    assert one_line_solution(word1, word2) == result
