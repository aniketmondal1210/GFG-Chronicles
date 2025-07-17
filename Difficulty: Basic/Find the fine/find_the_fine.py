#User function Template for python3
class Solution:
    def totalFine(self, date, car, fine):
        #Code here
        amt = 0
        if date % 2 == 0:
            for i in range(len(car)):
                if car[i] % 2 == 1:
                    amt += fine[i]
        else:
            for i in range(len(car)):
                if car[i] % 2 == 0:
                    amt += fine[i]
        return amt
