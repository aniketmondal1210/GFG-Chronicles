#User function Template for python3
class Solution:
    def solve(self, a):
        # code here
        b = list(set(a))
        vowels = ['a','e','i','o','u']
        count = 0
        for i in b:
            if i not in vowels:
                count += 1
        return "HE!" if count % 2 != 0 else "SHE!"
