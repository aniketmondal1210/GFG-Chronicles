"""index is the node which is to be displayed in output
  Node is defined as
class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
# Linked List class contains a Node object
class LinkedList:
    def __init__(self):
        self.head = None
This is method only submission.
 You only need to complete below method.
"""
class Solution:
    def GetNth(self, head, index):
        # Code Here
        idx = 1
        current = head
        while current:
            if idx == index:
                return current.data
            idx += 1
            current = current.next
        return -1
