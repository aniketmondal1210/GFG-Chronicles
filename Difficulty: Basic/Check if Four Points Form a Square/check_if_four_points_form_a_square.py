class Solution:
    def isSquare(self, points):    
        #code here
        def dist_sq(p1, p2):
            return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
        distances = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                distances.append(dist_sq(points[i], points[j]))
        distances.sort()
        if distances[0] == 0:
            return False
        return (
            distances[0] == distances[1]
            and distances[1] == distances[2]
            and distances[2] == distances[3]
            and distances[4] == distances[5]
            and distances[3] * 2 == distances[4]
        )
