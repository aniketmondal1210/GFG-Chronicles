class Solution:
    def sortedInsert(self, head, key):
        # code here
        # return head of edited linked list
        new_node = Node(key)
        
        if head is None or key < head.data:
            new_node.next = head
            return new_node
        
        current = head
        while current.next is not None and current.next.data < key:
            current = current.next
        new_node.next = current.next
        current.next = new_node
        return head
