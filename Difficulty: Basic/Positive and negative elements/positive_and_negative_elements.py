class Solution: 
    def arranged(self, arr: list[int]) -> list[int]: 
        # code here  
        pos = []
        neg = []
        for j in arr:
            if j > 0:
                pos.append(j)
            else:
                neg.append(j)
        res = []
        i = 0
        while i < len(pos) and i < len(neg):
            res.append(pos[i])
            res.append(neg[i])
            i += 1
        while i < len(pos):
            res.append(pos[i])
            i += 1
        while i < len(neg):
            res.append(neg[i])
            i += 1
        return res
