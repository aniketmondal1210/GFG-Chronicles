class Solution:
    def snakeCase(self, S , n):
        # code here
        S = S.replace(" ","_")
        return S.lower()
