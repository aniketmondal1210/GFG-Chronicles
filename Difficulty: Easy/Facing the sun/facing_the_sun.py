class Solution:
    # Returns count of buildings that can see sunlight
    def countBuildings(self, height):
        # code here
        count = 0
        max_height = 0
        for i in height:
            if i > max_height:
                count += 1
                max_height = i
        return count
