class Solution:
    def stringPartition(ob, S, a, b):
        # code here
        for i in range(1, len(S)):
            first_part = S[:i]
            second_part = S[i:]
            if int(first_part) % a == 0 and int(second_part) % b == 0:
                return first_part + " " + second_part
        return "-1"
