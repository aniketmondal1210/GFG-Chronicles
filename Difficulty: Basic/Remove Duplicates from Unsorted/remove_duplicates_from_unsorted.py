class Solution:
    def removeDuplicate(self, arr):
        # code here
        seen = set()
        result = []
        for i in arr:
            if i not in seen:
                seen.add(i)
                result.append(i)
        return result
