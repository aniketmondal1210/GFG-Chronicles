class Solution:
    def countryAtWar(self, arr1, arr2):
        # code here
        wins_a = 0
        wins_b = 0
        for i in range(len(arr1)):
            if arr1[i] > arr2[i]:
                wins_a += 1
            elif arr1[i] < arr2[i]:
                wins_b += 1
        if wins_a > wins_b:
            return "A"
        elif wins_b > wins_a:
            return "B"
        else:
            return "DRAW"
