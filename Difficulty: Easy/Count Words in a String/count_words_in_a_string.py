class Solution:
    def countWords(self, s: str) -> int:
        # code here
        s = s.replace('\t', ' ').replace('\n', ' ')
        a = s.split()
        return len(a)
