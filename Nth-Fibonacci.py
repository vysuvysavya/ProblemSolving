class Solution:
    def fib(self, n: int) -> int:
        if n <= 1 : return n
        a = 0
        b = 1
        while ( n > 1 ) :
            c = a+b
            a,b = b,c
            n -= 1
        return b

---------------------------

 def fib(self, n: int) -> int:
        if n<=1:
            return n
        elif n>1:
            return fib(n-1) + fib(n-2)

Input
n =
3
Output
2

0 1 1 2 3 5 ................
