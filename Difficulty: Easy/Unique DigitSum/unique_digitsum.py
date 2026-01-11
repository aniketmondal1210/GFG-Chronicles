class Solution:
    def uniqueDigitSums(self, arr):
        #code here
        result = []
        for j in arr:
            result.append(digitSum(j))
        return len(set(result))
        
def digitSum(n):
    summ = 0
    for i in str(n):
        summ += int(i)
    return summ
