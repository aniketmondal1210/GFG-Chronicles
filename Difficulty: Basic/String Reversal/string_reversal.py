# User function Template for python3
class Solution:
    def reverseString(self, s):
        # code here
        s = s.replace(" ", "")
        s = s[::-1]
        unique_chars = []
        for i in s:
            if i not in unique_chars:
                unique_chars.append(i)
        return ''.join(unique_chars)
