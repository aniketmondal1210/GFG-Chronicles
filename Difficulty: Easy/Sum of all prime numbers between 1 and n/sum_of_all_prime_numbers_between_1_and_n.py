#User function Template for python3
class Solution:
	def prime_Sum(self, n):
		# Code here
		summ = 0
		for i in range(1,n+1):
		    if is_prime(i):
		        summ += i
	    return summ
		
def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True
