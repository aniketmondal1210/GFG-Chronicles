#User function Template for python3
class Solution:
    def modify(self, s):
        # code here
        vowels = "aeiou"
        array = []
        for i in s:
            if i in vowels:
                array.append(i)
        array.reverse()
        new_s = ""
        idx = 0
        for j in s:
            if j in vowels:
                new_s += array[idx]
                idx += 1
            else:
                new_s += j
        return new_s
