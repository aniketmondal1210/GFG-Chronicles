class Solution:
    def removeCharacter(self, s: str, pos: int) -> str:
        # code here
        return s[:pos] + s[pos+1:]
