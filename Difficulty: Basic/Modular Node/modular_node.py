'''
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
class Solution:
    def modularNode(self, head, k):
        # Code Here
        result = []
        current = head
        while current:
            result.append(current.data)
            current = current.next
        maxi_data = -1
        for i in range(len(result)):
            if (i + 1) % k == 0:
                maxi_data = result[i]
        return maxi_data
