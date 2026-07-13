""" Node Structure
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
"""

class Solution:
    def compute(self, root):
        # code here
        result = []
        curr = root
        while curr:
            result.append(curr.data)
            curr = curr.next
        string = "".join(result)
        return string[::-1] == string
