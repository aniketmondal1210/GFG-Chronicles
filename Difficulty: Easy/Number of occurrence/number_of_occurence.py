class Solution:
    def countFreq(self, arr, target):
        #code here
        count = 0
        for i in arr:
            if i == target:
                count += 1
        return count

# Driver Code Starts
# Initial Template for Python 3
import bisect
#Main
if __name__ == "__main__":
    t = int(input())  # Number of test cases
    while t > 0:
        t -= 1
        A = list(map(int, input().strip().split()))
        D = list(map(int, input().strip().split()))
        
        ob = Solution()
        ans = ob.countFreq(A, D)
        print(ans)
        print("~")

# Driver Code Ends
    
