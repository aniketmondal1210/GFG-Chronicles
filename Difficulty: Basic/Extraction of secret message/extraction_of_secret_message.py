#User function Template for python3
class Solution:
    def ExtractMessage(self, s):
        # code here
        a = s.replace("LIE", " ")
        return " ".join(a.split())
