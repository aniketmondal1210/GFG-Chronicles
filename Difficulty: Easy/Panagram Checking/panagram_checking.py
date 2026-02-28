class Solution:
    def checkPangram(self,s):
        #code here
        letters = set(s.lower())
        print(letters)
        return len(letters.intersection(set('abcdefghijklmnopqrstuvwxyz'))) == 26
