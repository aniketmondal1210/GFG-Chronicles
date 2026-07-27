class Solution:
    def altCase(self, s):
        # code here
        first_char = s[0]
        result = []
        n = len(s)
        for i in range(n):
            if i % 2 == 0:
                if first_char.islower():
                    result.append(s[i].lower())
                else:
                    result.append(s[i].upper())
            else:
                if first_char.islower():
                    result.append(s[i].upper())
                else:
                    result.append(s[i].lower())
        return "".join(result)
