class Solution:
    def checkVectors(self, a1, a2, a3, b1, b2, b3):
        """ code here """
        dot_prod = a1 * b1 + a2 * b2 + a3 * b3
        x_i = (a2 * b3 - a3 * b2)
        y_j = (a1 * b3 - a3 * b1)
        z_k = (a1 * b2 - a2 * b1)
        cross_prod = x_i**2 + y_j**2 + z_k**2
        a = (a1 == 0) and (a2 == 0) and (a3 == 0)
        b = (b1 == 0) and (b2 == 0) and (b3 == 0)
        if a or b:
            return 0
        elif cross_prod == 0:
            return 1
        elif dot_prod == 0:
            return 2
        else:
            return 0
