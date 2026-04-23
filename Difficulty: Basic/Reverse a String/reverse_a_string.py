#User function Template for python3
class Solution:
     def reverseString(self, s: str) -> str:
        # code here
        a = list(s)
        left,right = 0,len(s)-1
        while(left<right):
            a[left],a[right] = a[right],a[left]
            left += 1
            right -= 1
        return "".join(a)
