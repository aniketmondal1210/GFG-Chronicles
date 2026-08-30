class Solution:
    def getMarks(self, l, r, rank):
        """code here"""
        marks = []
        for i in range(len(l)):
            marks.extend(range(l[i], r[i] + 1))
        result = []
        for j in rank:
            result.append(marks[j-1])
        return result
