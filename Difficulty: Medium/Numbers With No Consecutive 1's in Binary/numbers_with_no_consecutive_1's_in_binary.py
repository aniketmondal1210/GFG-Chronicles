class Solution:
	def noConsecutiveOnes(self, n):
		# code here
		result = []
        for i in range(1, 2**n):
            b = bin(i)[2:]
            if '11' not in b:
                result.append(i)
        return result
