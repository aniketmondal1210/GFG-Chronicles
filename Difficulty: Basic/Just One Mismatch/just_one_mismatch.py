#User function Template for python3
class Solution:
    def isStringExist (self, arr, N, S):
        # code here 
        def check_one_diff(s1, s2):
            if len(s1) != len(s2):
                return False
            diff = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    diff += 1
                    if diff > 1:
                        return False
            return diff == 1

        for i in arr:
            if check_one_diff(S,i):
                return "True"
        return "False"
