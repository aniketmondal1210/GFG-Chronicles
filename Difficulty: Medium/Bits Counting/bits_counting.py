from typing import List

class Solution:
    def countBits(self, n : int) -> List[int]:
        # code here
        result = []
        for i in range(n+1):
            result.append(ones_count(bin(i)[2:]))
        return result
        

def ones_count(n):
    return n.count('1')
