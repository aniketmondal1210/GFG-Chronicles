#User function Template for python3
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
def deleteAtPosition(head, pos):
    #code here
    if pos == 1:
        return head.next
    
    current = head
    for i in range(pos - 2):
        current = current.next
    current.next = current.next.next
    return head
