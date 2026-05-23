class Solution:
	def twoSum(self, arr, target):
		# code here
        seen = set()
        for i in arr:
            complement = target - i
            if complement in seen:
                return True
            seen.add(i)
        return False
