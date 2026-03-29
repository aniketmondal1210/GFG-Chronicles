'''    
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    def insertAtEnd(self, head, x):
        #code here 
        if head:
            current = head
            while current.next:
                current = current.next
            current.next = Node(x)
        else:
            head = Node(x)
        return head
