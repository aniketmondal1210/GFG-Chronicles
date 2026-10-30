class Solution:
    def checkIdentical(self, a: list[int], b: list[int]) -> bool:
        # code here 
        if len(a) != len(b):
            return False
        for i in range(len(a)):
            if a[i] != b[i]:
                return False
        return True
