class Solution:
    def sumExists(self, arr: list[int], sum: int) -> bool:
        # code here
        seen = set()
        for i in arr:
            if sum - i in seen:
                return True
            seen.add(i)
        return False
