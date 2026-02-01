#User function Template for python3
class Solution:
    def rearrange(self, arr):
        # code here
        pos = []
        neg = []
        
        for num in arr:
            if num >= 0:
                pos.append(num)
            else:
                neg.append(num)
        
        arr.clear()
        
        i, j = 0, 0
        while i < len(pos) and j < len(neg):
            arr.append(pos[i])
            arr.append(neg[j])
            i += 1
            j += 1
        
        while i < len(pos):
            arr.append(pos[i])
            i += 1
            
        while j < len(neg):
            arr.append(neg[j])
            j += 1
            
        return arr
