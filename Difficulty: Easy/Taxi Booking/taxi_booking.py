from typing import List
class Solution:
    def minimumTime(self, N : int, cur : int, pos : List[int], time : List[int]) -> int:
        # code here
        minn = float('inf')
        for i in range(N):
            minn = min(minn,abs(cur-pos[i])*time[i])
        return minn
