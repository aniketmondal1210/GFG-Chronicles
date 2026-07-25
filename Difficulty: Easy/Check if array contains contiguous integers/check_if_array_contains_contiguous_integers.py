class Solution:
    def areElementsContiguous (self, arr): 
    #Complete the function
        unique_elements = sorted(list(set(arr)))
        if len(unique_elements) <= 1:
            return True
        mini = unique_elements[0]
        maxi = unique_elements[-1]
        count = len(unique_elements)
        if maxi - mini + 1 == count:
            return True
        else:
            return False
