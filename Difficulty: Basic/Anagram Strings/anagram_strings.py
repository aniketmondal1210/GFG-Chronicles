#User function Template for python3
class Solution:
    def areAnagram(ob, S1, S2):
        # code here 
        if len(S1) != len(S2):
            return 0
        return 1 if sorted(S1) == sorted(S2) else 0
