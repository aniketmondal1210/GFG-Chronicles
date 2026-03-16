class Solution:
     def pattern(self, n):
        # code here
        ans = []
        solve(n,ans)
        return ans
        
def solve(number,ansList):
    ansList.append(number)
    if(number<=0):
        return 
    solve(number-5,ansList)
    ansList.append(number)
