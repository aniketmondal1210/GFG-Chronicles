from typing import List
class Solution:
    def insertAtBottom(self, st: List[int], x: int) -> List[int]:
        # code here
        st.insert(0, x)
        return st
