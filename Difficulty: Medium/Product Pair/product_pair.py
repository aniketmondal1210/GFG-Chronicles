class Solution:
    def isProduct(self, arr, target):
        # code here
        seen = set()
        for i in arr:
            if i == 0:
                if target == 0:
                    return True
            else:
                if target % i == 0 and target // i in seen:
                    return True
            seen.add(i)
        return False
