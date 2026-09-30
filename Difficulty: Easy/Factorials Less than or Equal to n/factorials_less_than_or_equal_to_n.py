class Solution:
    def factorialNumbers(self, n):
    	#code here 
    	result = []
        fact = 1
        i = 1
        while True:
            fact *= i
            if fact > n:
                break
            result.append(fact)
            i += 1
        return result
