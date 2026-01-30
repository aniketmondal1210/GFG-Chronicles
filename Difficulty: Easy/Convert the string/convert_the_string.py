#User function Template for python3
class Solution:
    def transform(self, Str):
        # code here
        vowels = ['A','E','I','O','U','a','e','i','o','u']
        result = ''
        for i in Str:
            if i not in vowels:
                if i.isupper():
                    result += '#' + i.lower()
                else:
                    result += '#' + i.upper()
        return result if result else "-1"
