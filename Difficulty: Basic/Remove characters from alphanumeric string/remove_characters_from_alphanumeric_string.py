#User function Template for python3
class Solution:
    def removeCharacters(self, s):
        # code here
        result = ""
        for char in s:
            if char.isdigit():
                result += char
        return result
