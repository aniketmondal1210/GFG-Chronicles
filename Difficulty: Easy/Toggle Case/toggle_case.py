class Solution:
    def toggleCase(self, s):
        # code here
        a = ""
        for i in s:
            if i.islower():
                a += i.upper()
            else:
                a += i.lower()
        return a
