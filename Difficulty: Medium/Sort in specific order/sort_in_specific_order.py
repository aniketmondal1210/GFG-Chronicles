class Solution:
    def sortIt(self, arr):
        # code here
        odd_numbers = [x for x in arr if x % 2 != 0]
        even_numbers = [x for x in arr if x % 2 == 0]
        odd_numbers.sort(reverse=True)
        even_numbers.sort()
        odd_numbers.extend(even_numbers)
        arr.clear()
        arr.extend(odd_numbers)
