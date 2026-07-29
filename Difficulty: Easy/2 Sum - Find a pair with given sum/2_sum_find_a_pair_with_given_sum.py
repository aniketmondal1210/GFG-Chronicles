class Solution:
    # Complete the below function
    def twoSum(self,arr, target):
        # Your code here
        seen = set()
        for i in arr:
            complement = target - i
            if complement in seen:
                return [complement, i]
            seen.add(i)
        return []
