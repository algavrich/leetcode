"""Given the head of a singly linked list, return the middle node of the
linked list.

If there are two middle nodes, return the second middle node.

>>> linked_list = LinkedList()
>>> linked_list.add_node_end(ListNode(1))
>>> linked_list.add_node_end(ListNode(2))
>>> linked_list.add_node_end(ListNode(3))
>>> linked_list.add_node_end(ListNode(4))
>>> linked_list.add_node_end(ListNode(5))
>>> linked_list.middle_node()
[3, 4, 5]

>>> linked_list.add_node_end(ListNode(6))
>>> linked_list.middle_node()
[4, 5, 6]

"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def add_node_end(self, node_to_add: ListNode) -> None:
        if self.head == None and self.tail == None:
            self.head = node_to_add
            self.tail = node_to_add
        elif self.head == self.tail:
            self.head.next = node_to_add
            self.tail = node_to_add
        else:
            self.tail.next = node_to_add
            self.tail = node_to_add

    def print_list(self) -> None:
        if self.head == None:
            return
        curr = self.head
        while curr:
            print(curr.val)
            curr = curr.next

    def middle_node(self) -> Optional[ListNode]:
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        ans = []
        while slow:
            ans.append(slow.val)
            slow = slow.next
        return ans


if __name__ == '__main__':
    import doctest
    doctest.testmod()