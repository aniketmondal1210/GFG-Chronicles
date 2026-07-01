class Solution:
    def reverse(self, s):
        # code here
        result = []
        for i in s:
            if i.isalpha():
                result.append(i)
        result.reverse()
        new_s = ""
        k = 0
        for j in range(len(s)):
            if s[j].isalpha():
                new_s += result[k]
                k += 1
            else:
                new_s += s[j]
        return new_s
