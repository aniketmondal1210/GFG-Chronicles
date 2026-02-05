#User function Template for python3
class Solution:
    def sortRecords(self, employee, salary):
        # Your code goes here
        a = sorted(zip(employee, salary), key=lambda x: (x[1], x[0]))
        return [emp for emp, sal in a]
