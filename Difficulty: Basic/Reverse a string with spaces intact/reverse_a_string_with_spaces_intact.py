class Solution:
    def reverses(self, s):
        # code here
        a = [i for i in s if i != " "]
        a.reverse()
        new_s = []
        idx = 0
        for j in range(len(s)):
            if s[j] == " ":
                new_s.append(" ")
            else:
                new_s.append(a[idx])
                idx += 1
        return "".join(new_s)
