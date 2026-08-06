class Solution:
    def studentRecord(self, l, N): 
        # code here 
        maxi = -1
        topper = []
        for i in range(N):
            name = l[i][0]
            m1 = int(l[i][1])
            m2 = int(l[i][2])
            m3 = int(l[i][3])
            avg = (m1+m2+m3)//3
            if avg > maxi:
                maxi = avg
                topper = [name]
            elif avg == maxi:
                topper.append(name)
        return " ".join(topper) + " " + str(maxi)
