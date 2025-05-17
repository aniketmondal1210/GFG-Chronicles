#User function Template for python3


class Solution:
    #Function to return a list containing the intersection of two arrays.
    def intersection(self, arr1, arr2):
        set1 = set(arr1)
        set2 = set(arr2)
        lst = list(set1 & set2)
        lst.sort()
        return lst

# { 
  # Driver Code Starts
# Initial Template for Python 3
import io
import sys
if __name__ == '__main__':
    test_cases = int(input())

    for _ in range(test_cases):
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))

        ob = Solution()
        res = ob.intersection(arr1, arr2)

        if len(res) > 0:
            print(*res)
        else:
            print("[]")
        print("~")
# } Driver Code Ends
