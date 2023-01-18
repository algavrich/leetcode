"""Given the head of a linked list, remove the nth node from the end of the
list and return its head.

>>> linked_list = LinkedList()
>>> linked_list.add_node_end(ListNode(1))
>>> linked_list.add_node_end(ListNode(2))
>>> linked_list.add_node_end(ListNode(3))
>>> linked_list.add_node_end(ListNode(4))
>>> linked_list.add_node_end(ListNode(5))
>>> linked_list.remove_nth_from_end(2)
[1, 2, 3, 5]

>>> linked_list = LinkedList()
>>> linked_list.add_node_end(ListNode(1))
>>> linked_list.remove_nth_from_end(1)
[]

>>> linked_list = LinkedList()
>>> linked_list.add_node_end(ListNode(1))
>>> linked_list.add_node_end(ListNode(2))
>>> linked_list.remove_nth_from_end(1)
[1]

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

    def remove_nth_from_end(self, n:int) -> List[int]:
        """First, intuitive solution. Accepted."""

        slow_prev = None
        slow = self.head
        fast = self.head

        for i in range(n):
            fast = fast.next

        while fast:
            slow_prev = slow
            slow = slow.next
            fast = fast.next

        if slow_prev == None:
            self.head = slow.next

        else:
            slow_prev.next = slow.next

        ans = []
        curr = self.head
        
        while curr:
            ans.append(curr.val)
            curr = curr.next
            
        return ans


if __name__ == '__main__':
    import doctest
    doctest.testmod()