class Solution:
    def ExtractNumber(self,sentence):
        #code here
        result = []
        maxx = -1
        words = sentence.split()
        for i in words:
            if i.isdigit():
                result.append(i)
        for j in result:
            if '9' not in j:
                maxx = max(int(j),maxx)
        return maxx 
