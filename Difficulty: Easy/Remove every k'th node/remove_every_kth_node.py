#Your task is to complete this function
#Your function should return the new head pointer
'''
class node:
    def __init__(self,x):
        self.data = x
        self.next = None
'''
class Solution:
    def deleteK(self, head, k):
        #code here  
        if k == 1:
            return None
        n = self.lengthLL(head)
        total = self.kthNodes(n, k)
        current = head
        prev = None
        count = 1
        while current:
            if count % k == 0:
                prev.next = current.next
                total -= 1
            else:
                prev = current
            current = current.next
            count += 1
        return head
        
    def lengthLL(self, head):
        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next
        return count

    def kthNodes(self, n, k):
        return n // k
