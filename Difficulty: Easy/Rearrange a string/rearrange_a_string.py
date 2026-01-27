#User function Template for python3
class Solution:
    def arrangeString(self, s):
        # code here
        nums = 0
        string = ''
        for i in s:
            if i.isdigit():
                nums += int(i)
            else:
                string += i
        string = ''.join(sorted(string))
        return string + str(nums) if nums > 0 else string
