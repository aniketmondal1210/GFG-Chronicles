class Solution:
    def printNumbers(self, n: int) -> list[int]:
        # code here
        result = []
        for i in range(1, n + 1):
            if i % 7 == 0:
                break
            if i % 3 == 0:
                continue
            result.append(i)
        return result
