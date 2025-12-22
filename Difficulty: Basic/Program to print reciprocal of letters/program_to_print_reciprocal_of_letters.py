#User function Template for python3
class Solution:
    def reciprocalString(self, S):
        # code here
        result = ''
        for char in S:
            if char.isupper():
                result += chr(ord('Z') + ord('A') - ord(char))
            elif char.islower():
                result += chr(ord('z') + ord('a') - ord(char))
            else:
                result += char
        return result
