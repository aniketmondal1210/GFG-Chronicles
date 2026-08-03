class Solution:
    def checkVectors(self, a1, a2, a3, b1, b2, b3):
        """ code here """
        dot_product = a1 * b1 + a2 * b2 + a3 * b3
        cx = a2 * b3 - a3 * b2
        cy = a3 * b1 - a1 * b3
        cz = a1 * b2 - a2 * b1
        cross_mag_squared = cx * cx + cy * cy + cz * cz
        a_is_zero = (a1 == 0 and a2 == 0 and a3 == 0)
        b_is_zero = (b1 == 0 and b2 == 0 and b3 == 0)
        if a_is_zero or b_is_zero:
            return 0
        if cross_mag_squared == 0:
            return 1
        elif dot_product == 0:
            return 2
        else:
            return 0
