#User function Template for python3
class Solution:
    def count(self,s):
    # your code here
        upp = 0
        low = 0
        num = 0
        spe = 0
        for i in s:
            if i.isdigit():
                num += 1
            elif i.isupper():
                upp += 1
            elif i.islower():
                low += 1
            elif not i.isalnum() and not i.isspace():
                spe += 1
        return upp,low,num,spe
