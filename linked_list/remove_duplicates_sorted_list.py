"""Given the head of a sorted linked list, delete all duplicates such that
each element appears only once. Return the linked list sorted as well.

>>> linked_list = LinkedList()
>>> linked_list.add_node_end(ListNode(1))
>>> linked_list.add_node_end(ListNode(1))
>>> linked_list.add_node_end(ListNode(2))
>>> linked_list.delete_duplicates()
[1, 2]

>>> linked_list.add_node_end(ListNode(3))
>>> linked_list.add_node_end(ListNode(3))
>>> linked_list.delete_duplicates()
[1, 2, 3]

"""

from typing import List


class ListNode:
    """Class definition for ListNode object."""

    def __init__(self, val: int=0, next=None) -> None:
        """Constructor for ListNode object."""

        self.val = val
        self.next = next


class LinkedList:
    """Class definition for LinkedList object."""

    def __init__(self) -> None:
        """Constructor for LinkedList object."""
        self.head = None
        self.tail = None

    def add_node_end(self, node_to_add: ListNode) -> None:
        """Add node to linked list."""

        if self.head == None and self.tail == None:
            self.head = node_to_add
            self.tail = node_to_add

        elif self.head == self.tail:
            self.head.next = node_to_add
            self.tail = node_to_add

        else:
            self.tail.next = node_to_add
            self.tail = node_to_add

    def delete_duplicates(self) -> List[int]:
        """First, intuitive solution. Accepted."""

        if not self.head or self.head.next == None:
            return self.head

        slow = self.head
        fast = self.head.next

        while fast and fast.next:
            if slow.val == fast.val:
                slow.next = fast.next
                fast = fast.next

            else:
                slow = slow.next
                fast = fast.next

        if slow.val == fast.val:
            slow.next = None

        ans = []
        curr = self.head

        while curr:
            ans.append(curr.val)
            curr = curr.next

        return ans


if __name__ == '__main__':
    import doctest
    doctest.testmod()