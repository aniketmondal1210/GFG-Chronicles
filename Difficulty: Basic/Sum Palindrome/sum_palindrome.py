class Solution:
    def isSumPalindrome (self, n):
        # code here 
        def is_palindrome(num):
            return str(num) == str(num)[::-1]
        def reverse_num(num):
            return int(str(num)[::-1])
        for i in range(5):
            if is_palindrome(n):
                return n
            rev_n = reverse_num(n)
            n += rev_n
            if is_palindrome(n):
                return n
        return -1
