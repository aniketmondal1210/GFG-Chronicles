#User function Template for python3
def isPalindrome(s):
    #Your code below
    #Remeber to ignore the case when comparing
    a = s.lower()
    return a[::-1] == a
