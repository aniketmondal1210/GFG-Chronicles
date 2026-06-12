class Solution:
    def transformString(self, s):
        # code here
        new_s = ""
        for i in s:
            if i.isupper():
                new_s += chr(ord('A') + ord('Z') - ord(i))
            else:
                new_s += chr(ord('a') + ord('z') - ord(i))
        return new_s
