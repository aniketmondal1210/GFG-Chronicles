#User function Template for python3
class Solution:
    # Function to find uncommon characters between two strings.
    def uncommonChars(self,s1, s2):
        set1 = set(s1)
        set2 = set(s2)
        uncommon_chars = (set1 | set2) - (set1 & set2)
        return ''.join(sorted(uncommon_chars))
