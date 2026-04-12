'''
class node:
    def __init__(self,data):
        self.data = data
        self.next = None
'''
class Solution:
    def getMiddle(self, head):
        # code here
        a = self.get_length(head)
        mid = a//2
        idx = 0
        current = head
        while idx < mid:
            current = current.next
            idx += 1
        return current.data
        
    def get_length(self,head):
        count = 0
        current = head
        while current:
            count += 1
            current = current.next
        return count
