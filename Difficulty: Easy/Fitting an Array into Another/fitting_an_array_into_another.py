class Solution:
    def isFit(self, a: list[int], b: list[int]) -> bool:
        # code here
        a.sort()
        b.sort()
        flag = True
        for i in range(len(a)):
            if a[i] > b[i]:
                flag = False
        return flag
