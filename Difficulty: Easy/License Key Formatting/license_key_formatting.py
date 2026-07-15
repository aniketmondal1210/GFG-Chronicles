class Solution:
    def reFormatString(self, s, k):
        # code here
        s = s.replace("-","")
        s = s[::-1]
        result = []
        for i in range(0, len(s), k):
            result.append(s[i:i+k])
        return "-".join(result)[::-1].upper()
