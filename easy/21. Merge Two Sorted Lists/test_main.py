import pytest

from main import LinkedList, merge


@pytest.mark.parametrize("list1, list2, ans", [
    (LinkedList([1, 2, 4]).head,
     LinkedList([1, 3, 4]).head,
     LinkedList([1, 1, 2, 3, 4, 4]).head),
])
def test_examples(list1, list2, ans):
    assert merge(list1, list2) == ans, f"{str(merge(list1,list2))=} \n {str(ans)=}"


def test_list_node_eq():
    a = LinkedList([1, 3, 4]).head
    b = LinkedList([1, 3, 4]).head
    assert a == b
    c = LinkedList([1, 3, 4, 5]).head
    assert a != c
