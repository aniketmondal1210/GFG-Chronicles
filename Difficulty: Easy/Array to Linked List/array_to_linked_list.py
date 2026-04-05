'''
# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    def arrayToList(self, arr):
        # code here
        head = None
        current = None
        for i in arr:
            new_node = Node(i)
            if not head:
                head = new_node
                current = new_node
            else:
                current.next = new_node
                current = current.next
        return head
