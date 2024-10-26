class Solution {
    static List<Integer> get(int a, int b) {
        // Step 1: Add both numbers and assign to a
        a = a + b;
        
        // Step 2: Subtract the new a by b to assign the value of original a to b
        b = a - b;
        
        // Step 3: Subtract the new a by the new b to assign the value of original b to a
        a = a - b;
        
        // Return the swapped values in a list
        return Arrays.asList(a, b);
    }
}
===================
Swap given two numbers and print them. (Try to do it without a temporary variable.) and return it.

Example 1:

Input: a = 13, b = 9
Output: 9 13
Explanation: after swapping it
becomes 9 and 13.
