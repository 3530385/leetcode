from task_67 import add_binary
import pytest

@pytest.mark.parametrize("a, b", [
    ("11", "1"),
    ("11", "10"),
    ("11", "0"),
    ("100", "11"),
    ])
def test_example(a,b):
    assert add_binary("11", "1") == "100"
