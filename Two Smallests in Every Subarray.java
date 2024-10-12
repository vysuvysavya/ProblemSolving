Given an array of integers arr, the task is to find and 
  return the maximum sum of the smallest and second smallest element among all possible subarrays of size greater than one. 
  If it is not possible, then return -1.

Examples:

Input: arr = [4, 3, 1, 5, 6]
Output: 11
Explanation: Subarrays with smallest and second smallest are,
Subarray: [4, 3], smallest = 3, second smallest = 4, sum = 7
Subarray: [4, 3, 1], smallest = 1, second smallest = 3, sum = 4
Subarray: [4, 3, 1, 5], smallest = 1, second smallest = 3, sum = 4
Subarray: [4, 3, 1, 5, 6], smallest = 1, second smallest = 3, sum = 4
Subarray: [3, 1], smallest = 1, second smallest = 3, sum = 4
Subarray: [3, 1, 5], smallest = 1, second smallest = 3, sum = 4
Subarray: [3, 1, 5, 6], smallest = 1, second smallest = 3, sum = 4
Subarray: [1, 5], smallest = 1, second smallest = 5, sum = 6
Subarray: [1, 5, 6] ,smallest = 1, second smallest = 5, sum = 6
Subarray: [5, 6], smallest = 5, second smallest = 6, sum = 11
Maximum sum among all above choices is, 5 + 6 = 11, hence the answer is 11.

=====================================================================================================

class Solution {
    public int pairWithMaxSum(int[] arr) {
        // If array has less than 2 elements, return -1
        if (arr.length < 2) {
            return -1;
        }
        
        int maxSum = Integer.MIN_VALUE;
        
        // Iterate through the array to find the maximum sum of consecutive pairs
        for (int i = 0; i < arr.length - 1; i++) {
            int currentSum = arr[i] + arr[i + 1];
            maxSum = Math.max(maxSum, currentSum);
        }
        
        return maxSum;
    }
}

====================================================================================

TC: O(n)

==================================================================================

Key Observation:
Although the problem mentions finding the "smallest" and "second smallest" elements in all subarrays, 
  the largest sum for such elements will always come from consecutive elements. Here's why:

Why Consecutive Pairs Work:
When you consider subarrays of size greater than 1, the smallest and second smallest elements are usually adjacent in some subarray. This is because:

Adjacent pairs are the most straightforward subarrays of size 2.
In larger subarrays (size > 2), the smallest two elements can also be adjacent.
The largest possible sum of the smallest and second smallest elements across all subarrays is often formed by consecutive elements, simply because:
- The second smallest element in a larger subarray is unlikely to increase the sum if it’s far from the smallest element.
- If two numbers are adjacent, they naturally cover all subarrays that include them.
