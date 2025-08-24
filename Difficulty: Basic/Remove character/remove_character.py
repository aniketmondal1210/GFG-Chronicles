#User function Template for python3
class Solution:
    def removeChars(self, str1, str2):
        # code here
        str2_set = set(str2)
        result = ''
        for char in str1:
            if char not in str2_set:
                result += char
        return result
