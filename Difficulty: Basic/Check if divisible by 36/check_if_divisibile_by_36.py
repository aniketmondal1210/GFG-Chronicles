# User function Template for python3
class Solution:
    def checkDivisible36(self, S):
        return 1 if (self.divisible_by_4(S) and self.divisible_by_9(S)) else 0

    def divisible_by_4(self, x):
        if len(x) >= 2:
            last_two = int(x[-2:])
        else:
            last_two = int(x)
        return last_two % 4 == 0

    def divisible_by_9(self, y):
        digit_sum = sum(int(ch) for ch in y)
        return digit_sum % 9 == 0
