'''
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
class Solution:
    def sumOfLastN_Nodes(self, head, n):
        #function should return sum of last n nodes
        length = self.length_ll(head)
        idx = length - n
        count = 0
        current = head
        summ = 0
        while count < idx:
            count += 1
            current = current.next
    
        while current:
            summ += current.data
            current = current.next
        
        return summ
        
    def length_ll(self, head):
        idx = 0
        current = head
        while current:
            idx += 1
            current = current.next
        return idx
