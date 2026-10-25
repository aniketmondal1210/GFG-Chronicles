class Solution:
    def rearrange(self, arr):
        # code here
        temp = arr[:]
        result = []
        while temp:
            maxi = max(temp)
            temp.remove(maxi)
            result.append(maxi)
            if temp:
                mini = min(temp)
                temp.remove(mini)
                result.append(mini)
        for i in range(len(arr)):
            arr[i] = result[i]
