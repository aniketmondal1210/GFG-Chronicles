class Solution:
    def countVowels(self, s):
        #code here
        vowels = {'a', 'e', 'i', 'o', 'u'}
        seen = set()
        for i in s:
            if i in vowels:
                seen.add(i)
        return len(seen)
