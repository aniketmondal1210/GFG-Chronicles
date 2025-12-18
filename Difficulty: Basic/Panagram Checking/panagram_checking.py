class Solution:
    def isPanagram(self,s):
        #your code here
        a = set('abcdefghijklmnopqrstuvwxyz')
        seen = set()
        for i in s.lower():
            if i not in seen:
                seen.add(i)
        return a == seen
