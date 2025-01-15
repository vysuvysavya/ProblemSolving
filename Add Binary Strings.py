class Solution:
    def addBinary(self, s1, s2):
        i, j = len(s1) - 1, len(s2) - 1
        carry = 0
        result = []
        
        while i >= 0 or j >= 0 or carry:
            digit1 = int(s1[i]) if i >= 0 else 0
            digit2 = int(s2[j]) if j >= 0 else 0
            
            total = digit1 + digit2 + carry
            result.append(str(total % 2))
            carry = total // 2
            
            i -= 1
            j -= 1
        
        return ''.join(result[::-1]).lstrip('0') or "0"

=======================================

Given two binary strings s1 and s2 consisting of only 0s and 1s. Find the resultant string after adding the two Binary Strings.
Note: The input strings may contain leading zeros but the output string should not have any leading zeros.

Input: s1 = "1101", s2 = "111"
Output: 10100
Explanation:
 1101
+ 111
10100
Input: s1 = "00100", s2 = "010"
Output: 110
Explanation: 
  100
+  10
  110
