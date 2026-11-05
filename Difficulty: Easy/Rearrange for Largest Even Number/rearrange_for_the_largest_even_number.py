class Solution:
    def largestEven(self, s):
        # code here
        digits = sorted(list(s), reverse=True)
        if int(digits[-1]) % 2 == 0:
            return "".join(digits)
        even_digits = [int(d) for d in digits if int(d) % 2 == 0]
        if not even_digits:
            return "".join(digits)
        smallest_even = min(even_digits)
        digits.remove(str(smallest_even))
        return "".join(digits) + str(smallest_even)
