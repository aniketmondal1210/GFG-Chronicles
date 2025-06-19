class Solution:
    def print_even_indices(self, s: str):
        #code here
        for i in range(0,len(s),2):
            print(s[i],end="")
