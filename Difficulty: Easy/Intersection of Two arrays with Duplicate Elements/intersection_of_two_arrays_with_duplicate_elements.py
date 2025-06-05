
class Solution:
    def intersectionWithDuplicates(self, a, b):
        # code here
        set_a = set(a)
        set_b = set(b)
        intersection = set_a & set_b
        return list(intersection)
