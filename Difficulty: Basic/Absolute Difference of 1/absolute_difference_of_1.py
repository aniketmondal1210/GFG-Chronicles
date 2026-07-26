class Solution:
    def getDigitDiff1AndLessK(self, arr: list[int], k: int) -> list[int]:
        # code here
        def has_diff_one(n):
            s = str(n)
            if len(s) < 2:
                return False
            for j in range(len(s) - 1):
                if abs(int(s[j]) - int(s[j+1])) != 1:
                    return False
            return True
        result = []
        for i in arr:
            if i < k and has_diff_one(i):
                result.append(i)
        return result
