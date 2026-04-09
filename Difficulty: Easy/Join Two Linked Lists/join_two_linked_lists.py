'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    def joinTheLists(self, head1, head2):
       # code here
        if not head1:
            return head2
        if not head2:
            return head1
            
        current1 = head1
        while current1.next:
            current1 = current1.next
        current1.next = head2
        return head1
