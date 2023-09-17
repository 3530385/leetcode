from task_67 import add_binary, add_binary_my
import pytest

@pytest.mark.parametrize("a, b", [
    ("11", "1"), ("11", "10"),
    ("11", "0"),
    ("100", "11"),
    ])
def test_example(a:str, b:str):
    assert add_binary_my(a,b)== add_binary(a,b)
