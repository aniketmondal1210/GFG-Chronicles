#User function Template for python3
class Solution:
    # Function to convert the given string to Camel Case
    def convertToCamelCase(self, s):
        # code here
        words = s.split()
        result = words[0]  
        for word in words[1:]:
            result += word.title()
        return result
