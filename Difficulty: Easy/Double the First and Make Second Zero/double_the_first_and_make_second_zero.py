class Solution:
    def modifyArray(self, arr): 
        #code here
        n = len(arr)
        for i in range(n - 1):
            if arr[i] == arr[i+1] and arr[i] != 0:
                arr[i] *= 2
                arr[i+1] = 0
        non_zeros = [x for x in arr if x != 0]
        arr[:] = non_zeros + [0] * (n - len(non_zeros))
        return arr
