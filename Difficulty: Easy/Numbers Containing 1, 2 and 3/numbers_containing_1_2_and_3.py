class Solution:
    def filterByDigits(self, arr):
        #code here
        result = []
        allowed = set("123")
        for i in arr:
            if set(str(i)) <= allowed:
                result.append(i)
        return result if result else [-1]
