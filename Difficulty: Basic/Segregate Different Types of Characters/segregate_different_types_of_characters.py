class Solution:
    def splitString(self, s): 
        # code here 
        letters = []
        digits = []
        specials = []
        for i in s:
           if i.isalpha():
               letters.append(i)
           elif i.isdigit():
               digits.append(i)
           else:
               specials.append(i)
        s1 = ''.join(letters) if letters else "-1"
        s2 = ''.join(digits) if digits else "-1"
        s3 = ''.join(specials) if specials else "-1"
        return [s1, s2, s3]
