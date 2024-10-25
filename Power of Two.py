Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two, if there exists an integer x such that n == 2x.

Example 1:

Input: n = 1
Output: true
Explanation: 20 = 1
Example 2:

Input: n = 16
Output: true
Explanation: 24 = 16
=====================================================================================
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:  
        return n > 0 and (n & (n - 1)) == 0
//And operation between multiple of 2 and next lower number will always give 0 and other wise it will never be 0.

example 1: 8 & 7
1000(8) & 0111(7) => 0000(0)

example 1: = 10 & 9
1010(10) & 1001(9) => 1000(8)
---
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        for i in range(31):
            ans = 2 ** i
            if ans == n:
                return True
        return False
