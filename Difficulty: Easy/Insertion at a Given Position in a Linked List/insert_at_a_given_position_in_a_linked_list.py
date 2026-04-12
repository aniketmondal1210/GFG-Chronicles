'''
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''
class Solution:
    def insertPos(self, head, pos, val):
        # code here
        new_node = Node(val)
        
        if pos == 1:
            new_node.next = head
            return new_node
            
        current = head
        for i in range(1,pos-1):
            current = current.next
        
        new_node.next = current.next
        current.next = new_node
        
        return head
