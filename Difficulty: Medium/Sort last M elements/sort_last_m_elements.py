#User function Template for python3
class Solution:
    def sortLastMelements(self, nums, n, m):
        last_m_elements = nums[n:n + m]
        last_m_elements.sort()
        nums[n:n + m] = last_m_elements
