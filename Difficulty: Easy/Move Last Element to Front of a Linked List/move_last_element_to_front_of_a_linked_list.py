from typing import Optional

"""
Definition for singly Link List Node
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

You can also use the following for printing the link list.
printList(node)
"""
class Solution:
    def moveToFront(self, head : Optional['Node']) -> Optional['Node']:
        # code here
        if not head or not head.next:
            return head
        current = head
        while current.next.next:
            current = current.next
        last_node = current.next
        current.next = None
        last_node.next = head
        return last_node
