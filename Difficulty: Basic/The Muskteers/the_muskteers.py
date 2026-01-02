#User function Template for python3
class Solution:
    def checkTogether(self, str):
        # code here
        a = str.count('0')
        if a == 0:
            return False
        b = str.find('0')
        substr = str[b:b+a]
        if substr == '0'*a:
            return True
        else:
            return False
