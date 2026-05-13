class Solution:
    def reverse(self, s: str) -> str:
        #code here 
        stack = []
        for char in s:
            stack.append(char)
        reversed_s = ""
        while stack:
            reversed_s += stack.pop()
        return reversed_s
