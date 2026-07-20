class Solution:
    def findGreatest(self, arr):
        # code here
        arr.sort(reverse=True)
        n = len(arr)
        for i in range(n):
            target = arr[i]
            seen = set()
            for j in range(n):
                if i == j:
                    continue
                if target % arr[j] == 0:
                    complement = target // arr[j]
                    if complement in seen:
                        return target
                seen.add(arr[j])
        return -1
