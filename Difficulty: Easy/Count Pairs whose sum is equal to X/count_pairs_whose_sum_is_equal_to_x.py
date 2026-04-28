'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
'''
    head1:  head of linkedList 1
    head2:  head of linkedList 2
    n1:  len of  linkedList 1
    n2:  len of linkedList 1
    x:   given sum
'''
class Solution:
    def countPairs(self, head1, head2, x):
        # code here
        elements_set = set()
        current = head1
        while current:
            elements_set.add(current.data)
            current = current.next
        
        count = 0
        current = head2
        while current:
            target = x - current.data
            if target in elements_set:
                count += 1
            current = current.next
            
        return count
