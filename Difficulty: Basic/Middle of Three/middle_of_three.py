import numpy as np
#User function Template for python3
class Solution:
    def middle(self, a, b, c):
        #code here
        if a > b:
            if b > c:
                return b  # a > b > c
            elif a > c:
                return c  # a > c > b
            else:
                return a  # b > a > c
        else:
            if a > c:
                return a  # b > a > c
            elif b > c:
                return c  # b > c > a
            else:
                return b  # c > b > a
