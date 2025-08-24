class Solution:
    def reverseWords(self, s: str) -> str:
        #code here
        s.strip()
        words = s.split()
        new_s = ""
        for i in words:
            new_s += (i[::-1] + " ")
        return new_s[:-1]
