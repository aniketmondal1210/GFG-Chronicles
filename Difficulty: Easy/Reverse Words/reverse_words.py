# User function Template for python3

class Solution:
    # Function to reverse words in a given string.
    def reverseWords(self, s):
        # code here 
        s.strip()
        result = ""
        words = s.split()
        for i in words[::-1]:
            result += (i + " ")
        return result[:-1]
