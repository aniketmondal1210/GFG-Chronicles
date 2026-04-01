'''
    Your task is to insert a new node in 
	the middle of the linked list with
	the given value.
	
	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
	
	Function Arguments: head (head of linked list), node 
	(node to be inserted in middle)
	Return Type: None, just insert the new node at mid.
'''
#Function to insert a node in the middle of the linked list.
class Solution:
    def insertInMiddle(self, head, x):
        #code here
        if head is None:
            return Node(x)
        length = self.findLength(head)
        mid = (length - 1) // 2
        new_node = Node(x)
        current = head
        count = 0
        while count < mid:
            current = current.next
            count += 1
        new_node.next = current.next
        current.next = new_node
        return head
    
    def findLength(self, head):
        count = 0
        current = head
        while current:
            count += 1
            current = current.next
        return count
