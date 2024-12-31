Project Euler #5: Smallest multiple
Problem
Submissions
Leaderboard
Discussions
This problem is a programming version of Problem 5 from projecteuler.net

 is the smallest number that can be divided by each of the numbers from  to  without any remainder.
What is the smallest positive number that is evenly divisible(divisible with no remainder) by all of the numbers from  to ?

Input Format

First line contains  that denotes the number of test cases. This is followed by  lines, each containing an integer, .

Constraints

Output Format

Print the required answer for each test case.

Sample Input 0

2
3
10
Sample Output 0

6
2520
Explanation 0

You can check  is divisible by each of , giving quotient of  respectively.
You can check  is divisible by each of  giving quotient of  respectively.
Submissions: 39
Max Score: 30
Difficulty: Medium
Rate This Challenge:

  #!/bin/python3

import sys
import math

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    result = 1
    for i in range(1, n + 1):
        result = result * i // math.gcd(result, i)
    print(result)
