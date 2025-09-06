#User function Template for python3
class Solution:
    def removeConsonants(self, s):
        #complete the function here
        new_s = ""
        vowels = "aeiouAEIOU"
        for i in s:
            if i in vowels:
                new_s += i
        return new_s if len(new_s) != 0 else "No Vowel"
