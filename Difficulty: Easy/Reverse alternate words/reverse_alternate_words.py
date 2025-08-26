#User function Template for python3
class Solution:
    def reverseAlternate(self, strr):
        # code here
        new_words = ""
        words = strr.split()
        for i in range(len(words)):
            if i % 2 != 0:
                new_words += ((words[i])[::-1] + " ")
            else:
                new_words += (words[i] + " ")
        return new_words.strip()
