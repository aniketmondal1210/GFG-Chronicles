class Solution:
    def lcmAndGcd(self, a : int, b : int) -> List[int]:
        return [lcm(a, b), hcf(a, b)]
        
def hcf(a,b):
    while b:
        a,b = b, a % b
    return a
            
def lcm(a,b):
    return abs(a*b)//hcf(a,b)
