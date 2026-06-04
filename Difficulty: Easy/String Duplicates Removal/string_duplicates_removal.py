# User function Template for python3
class Solution:
    def removeDuplicates(self, s):
        # code here
        seen = set()
        result = []
        for i in s:
            if i not in seen:
                seen.add(i)
                result.append(i)
        return "".join(result)
