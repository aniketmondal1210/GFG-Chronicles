""" Node Structure
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
"""

class Solution:
    def deleteMid(self, head):
        # code here
        if not head or not head.next:
            return None
        mid = self.length_ll(head)//2
        count = 0
        curr = head
        while count < mid - 1:
            count += 1
            curr = curr.next
        curr.next = curr.next.next
        return head
        
    def length_ll(self,head):
        len = 0
        curr = head
        while curr:
            len += 1
            curr = curr.next
        return len
