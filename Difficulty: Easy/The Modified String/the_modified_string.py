class Solution:
    def modified(self, s):
        #code here
        insertions = 0
        run = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                run += 1
            else:
                run = 1
            if run == 3:
                insertions += 1
                run = 1
        return insertions
