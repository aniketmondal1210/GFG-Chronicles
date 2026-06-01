#User function Template for python3
class Solution:
    def search(self, pat, txt):
        # code here
        pat = pat.lower()
        txt = txt.lower()
        result = []
        for i in range(len(txt) - len(pat) + 1):
            if txt[i:i + len(pat)] == pat:
                result.append(i)
        return result
