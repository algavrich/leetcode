"""Given the head of a singly linked list, reverse the list, and return the
reversed list.

>>> linked_list = LinkedList()
>>> linked_list.add_node_end(ListNode(1))
>>> linked_list.add_node_end(ListNode(2))
>>> linked_list.add_node_end(ListNode(3))
>>> linked_list.add_node_end(ListNode(4))
>>> linked_list.add_node_end(ListNode(5))
>>> linked_list.reverse_list()
[5, 4, 3, 2, 1]

>>> linked_list2 = LinkedList()
>>> linked_list2.add_node_end(ListNode(1))
>>> linked_list2.add_node_end(ListNode(2))
>>> linked_list2.reverse_list()
[2, 1]

>>> linked_list3 = LinkedList()
>>> linked_list3.reverse_list()
[]

"""

from typing import List


class ListNode:
    """Class definition for ListNode object."""

    def __init__(self, val=0, next=None) -> None:
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

    def reverse_list(self) -> List[int]:
        """First, intuitive solution. Accepted.""" 

        prev = None
        curr = self.head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        ans = []
        curr = prev

        while curr:
            ans.append(curr.val)
            curr = curr.next
            
        return ans


if __name__ == '__main__':
    import doctest
    doctest.testmod()