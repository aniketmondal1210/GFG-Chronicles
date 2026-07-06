class Solution:
    def missingPanagram(self, s):
        # code here
        s = s.lower()
        missing = set('abcdefghijklmnopqrstuvwxyz') - set(s)
        return "".join(sorted(missing)) if missing else -1
