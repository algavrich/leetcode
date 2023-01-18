"""You are given the head of a linked list. Delete the middle node, and
return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the
start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than
or equal to x.

>>> linked_list = LinkedList()
>>> linked_list.add_node_end(ListNode(1))
>>> linked_list.add_node_end(ListNode(3))
>>> linked_list.add_node_end(ListNode(4))
>>> linked_list.add_node_end(ListNode(7))
>>> linked_list.add_node_end(ListNode(1))
>>> linked_list.add_node_end(ListNode(2))
>>> linked_list.add_node_end(ListNode(6))
>>> linked_list.delete_middle()
[1, 3, 4, 1, 2, 6]

>>> linked_list = LinkedList()
>>> linked_list.add_node_end(ListNode(1))
>>> linked_list.add_node_end(ListNode(2))
>>> linked_list.add_node_end(ListNode(3))
>>> linked_list.add_node_end(ListNode(4))
>>> linked_list.delete_middle()
[1, 2, 4]

>>> linked_list = LinkedList()
>>> linked_list.add_node_end(ListNode(2))
>>> linked_list.add_node_end(ListNode(1))
>>> linked_list.delete_middle()
[2]

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

    def delete_middle(self) -> List[int]:
        """First, intuitive solution. Accepted."""

        if not self.head.next:
            return None
        
        slow_prev = None
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow_prev = slow
            slow = slow.next
            fast = fast.next.next

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