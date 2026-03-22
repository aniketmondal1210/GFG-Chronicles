class Solution:
    def caseSort(self,s):
        #code here
        upper = []
        lower = []
        for i in s:
            if i.isupper():
                upper.append(i)
            else:
                lower.append(i)
        upper.sort()
        lower.sort()
        upper_j = 0
        lower_j = 0
        new_s = []
        for k in s:
            if k.isupper():
                new_s.append(upper[upper_j])
                upper_j += 1
            else:
                new_s.append(lower[lower_j])
                lower_j += 1
        return ''.join(new_s)
