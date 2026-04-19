'''
    {
        # Node Class
        class Node:
            def __init__(self, data):   # data -> value stored in node
                self.data = data
                self.next = None
    }
'''
class Solution:
    def getKthFromLast(self, head, k):
        length = self.length_ll(head)
        if k > length:
            return -1
        position = length - k
        current = head
        while position > 0:
            current = current.next
            position -= 1
        return current.data

    def length_ll(self, head):
        count = 0
        current = head
        while current:
            count += 1
            current = current.next
        return count
