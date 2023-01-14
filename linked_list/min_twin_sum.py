"""In a linked list of size n, where n is even, the ith node (0-indexed) of
the linked list is known as the twin of the (n-1-i)th node,
if 0 <= i <= (n / 2) - 1.

For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the
twin of node 2. These are the only nodes with twins for n = 4.
The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the maximum twin sum
of the linked list.

>>> linked_list = LinkedList()
>>> linked_list.add_node_end(ListNode(5))
>>> linked_list.add_node_end(ListNode(4))
>>> linked_list.add_node_end(ListNode(2))
>>> linked_list.add_node_end(ListNode(1))
>>> linked_list.pair_sum()
6

>>> linked_list = LinkedList()
>>> linked_list.add_node_end(ListNode(4))
>>> linked_list.add_node_end(ListNode(2))
>>> linked_list.add_node_end(ListNode(2))
>>> linked_list.add_node_end(ListNode(3))
>>> linked_list.pair_sum()
7

>>> linked_list = LinkedList()
>>> linked_list.add_node_end(ListNode(1))
>>> linked_list.add_node_end(ListNode(100000))
>>> linked_list.pair_sum()
100001

"""


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

    def pair_sum(self) -> int:
        """First, intuitive solution using fast and slow pointers and reversal.
        Accepted."""
        
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        pointer1 = prev
        pointer2 = self.head
        ans = 0
        while pointer1:
            ans = max(ans, pointer1.val + pointer2.val)
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        return ans


if __name__ == '__main__':
    import doctest
    doctest.testmod()