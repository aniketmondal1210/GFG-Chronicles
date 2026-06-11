from collections import Counter
class Solution:
    def moreFrequent(self, arr, x, y):
        #code here
        a = Counter(arr)
        count_x = a[x]
        count_y = a[y]
        if count_x == count_y:
            return min(x, y)
        return x if count_x > count_y else y
