#User function Template for python3
class Solution:
	def balancedNumber(self, N):
		# your code here
        n = len(str(N))
        left_sum = 0
        right_sum = 0
        for i in range(n//2):
            left_sum += int(str(N)[i])
        for i in range(n//2 + 1, n):
            right_sum += int(str(N)[i])
        return left_sum == right_sum
