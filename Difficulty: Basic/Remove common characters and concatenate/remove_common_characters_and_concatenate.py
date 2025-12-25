class Solution:
    def concatenatedString(self,s1,s2):
        #code here
        a = set(s1)
        b = set(s2)
        c = a.intersection(b)
        result1 = [i for i in s1 if i not in c]
        result2 = [j for j in s2 if j not in c]
        net_result = result1 + result2
        return ''.join(net_result) if len(net_result) > 0 else -1
