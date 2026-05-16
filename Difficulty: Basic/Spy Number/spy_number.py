class Solution:
    def checkSpy(self, n):
        # code here
        result = [int(d) for d in str(n)]
        digit_sum = sum(result)
        digit_product = 1
        for i in result:
            digit_product *= i
        return digit_sum == digit_product
