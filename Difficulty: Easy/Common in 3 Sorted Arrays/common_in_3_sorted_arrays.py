#User function Template for python3
class Solution:
    def commonElements(self, arr1, arr2, arr3):
        #Code Here
        set_1 = set(arr1)
        set_2 = set(arr2)
        set_3 = set(arr3)
        int_1 = set_1.intersection(set_2)
        int_2 = int_1.intersection(set_3)
        return sorted(list(int_2))
