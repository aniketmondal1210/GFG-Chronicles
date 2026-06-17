class Solution:
    def SandwichedVowel(self, s):
        # code here
        vowels = {'a', 'e', 'i', 'o', 'u'}
        if len(s) < 3:
            return s
        result = []
        for i in range(len(s)):
            char = s[i]
            if char in vowels and i > 0 and i < len(s) - 1:
                if s[i-1] not in vowels and s[i+1] not in vowels:
                    continue
            result.append(char)
        return "".join(result)
