class Solution:
    # your task is to complete this function
    # function should return false if length is even
    # else return true
    def isLengthEven(self, head):
        # Code here
        current = head
        result = []
        while current:
            result.append(current.data)
            current = current.next
        return len(result) % 2 == 0
