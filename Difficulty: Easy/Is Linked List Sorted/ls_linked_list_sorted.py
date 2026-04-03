'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    def isSorted(self, head):
        # code here
        result = []
        current = head
        while current:
            result.append(current.data)
            current = current.next
        a = result.copy()
        b = result.copy()
        a.sort()
        b.sort(reverse=True)
        return a == result or b == result
