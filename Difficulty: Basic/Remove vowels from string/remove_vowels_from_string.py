#User function Template for python3
class Solution:
    def removeVowels(self, s):
        vowels = 'aeiou'
        new_s = ""
        for ch in s:
            if ch not in vowels:
                new_s += ch
        return new_s
