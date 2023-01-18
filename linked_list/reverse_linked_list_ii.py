"""Given the head of a singly linked list and two integers left and right
where left <= right, reverse the nodes of the list from position left to
position right, and return the reversed list.

>>> linked_list = LinkedList()
>>> linked_list.add_node_end(ListNode(1))
>>> linked_list.add_node_end(ListNode(2))
>>> linked_list.add_node_end(ListNode(3))
>>> linked_list.add_node_end(ListNode(4))
>>> linked_list.add_node_end(ListNode(5))
>>> linked_list.reverse_between(2, 4)
[1, 4, 3, 2, 5]

>>> linked_list2 = LinkedList()
>>> linked_list2.add_node_end(ListNode(5))
>>> linked_list2.reverse_between(1, 1)
[5]

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

    def reverse_between(self, left: int, right: int) -> List[int]:
        """First, intuitive solution. Accepted."""

        if not self.head.next:
            return [self.head.val]

        if left == right:
            ans = []
            curr = self.head

            while curr:
                ans.append(curr.val)
                curr = curr.next
                
            return ans

        prev = None
        curr = self.head
        idx = 1

        while idx != left:
            prev = curr
            curr = curr.next
            idx += 1

        left_prev = prev
        left_node = curr
        prev = curr
        curr = curr.next
        idx += 1

        while idx != right:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            idx += 1

        next_node = curr.next
        curr.next = prev

        if left_prev == None:
            self.head = curr

        else:
            left_prev.next = curr

        left_node.next = next_node
        
        ans = []
        curr = self.head

        while curr:
            ans.append(curr.val)
            curr = curr.next
            
        return ans

if __name__ == '__main__':
    import doctest
    doctest.testmod()