class Solution:
	def makeZero(self, arr: list[int]) -> bool:
		""" code here """
		result = 0
        for i in arr:
            result ^= i
        if result == 0:
            return False
        return len(arr) % 2 != 0
