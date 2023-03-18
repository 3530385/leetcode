from time_compexity_plot.plot import plot_time_complexity


class ListNode(object):
    def __init__(self, val: int = 0, next: object = None):
        self.val = val
        self.next = next

    def __str__(self):
        printed_list = [self.val]
        node = self.next
        while node:
            printed_list.append(node.val)
            node = node.next
        return str(printed_list)

    def __eq__(self, other):
        head1 = self
        head2 = other
        while head1 and head2 and head1.val == head2.val:
            head1 = head1.next
            head2 = head2.next
        return head1 is head2


class LinkedList:
    def __init__(self, nums: list = []):
        self.head = ListNode(nums[0]) if nums else None
        cache = self.head
        for i in range(1, len(nums)):
            cache.next = ListNode(nums[i])
            cache = cache.next

    def __str__(self):
        if self.head:
            return str(self.head)
        return str([])


def merge(list1: ListNode, list2: ListNode) -> object | None:
    cur = dummy = ListNode()
    while list1 and list2:
        if list1.val < list2.val:
            cur.next = list1
            list1, cur = list1.next, list1
        else:
            cur.next = list2
            list2, cur = list2.next, list2

    if list1 or list2:
        cur.next = list1 if list1 else list2

    return dummy.next


def plotting_function(n):
    a = LinkedList(list(range(n // 2)))
    b = LinkedList(list(range(n // 2)))
    # print(a is b)
    merge(a.head, b.head)


if __name__ == '__main__':
    plot_time_complexity(plotting_function, 10, 10**5, 10*4, 3)