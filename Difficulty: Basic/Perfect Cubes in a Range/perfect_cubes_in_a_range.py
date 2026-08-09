class Solution:
    def properCubes(self, a, b):
        # code here
        result = []
        i = 1
        while i**3 <= b:
            if i**3 >= a:
                result.append(i**3)
            i += 1
        return result if result else [-1]
