'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    def deleteNode(self, head, x):
        #code here
        if x == 1:
            return head.next
        current = head
        for i in range(1,x-1):
            current = current.next
        current.next = current.next.next
        return head
