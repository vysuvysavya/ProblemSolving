
class Solution:
    def lcmAndGcd(self, A, B):
        # code here 
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a
        gcd = gcd(A, B)
        lcm = (A * B) // gcd
        return [lcm, gcd]
