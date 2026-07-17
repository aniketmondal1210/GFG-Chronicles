class Solution:
    def smallerAndLarge(self, s):
        # code here
        a = s.split()
        mini = float('inf')
        min_word = ""
        maxi = 0
        max_word = ""
        for i in a:
            if len(i) >= maxi:
                max_word = i
                maxi = len(i)
            if len(i) < mini:
                min_word = i
                mini = len(i)
        return [min_word,max_word]
