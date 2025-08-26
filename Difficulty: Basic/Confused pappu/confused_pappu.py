#User function Template for python3
class Solution:
    def findDiff(self, amount):
        # code here
        a = 0
        if '6' in str(amount):
            a += int(str(amount).replace('6','9'))
        elif '9' in str(amount):
            a += int(str(amount).replace('9','6'))
        else:
            a = amount
        return abs(a - amount)
