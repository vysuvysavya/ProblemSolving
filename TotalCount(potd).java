You are given an array arr[] of positive integers and a threshold value k.
  For each element in the array, 
  divide it into the minimum number of small integers such that each divided integer is less than or equal to k. Compute the total number of these integer across all elements of the array.

Examples:

Input: k = 3, arr[] = [5, 8, 10, 13]
Output: 14
Explanation: Each number can be expressed as sum of different numbers less than or equal to k as
  5 (3 + 2), 8 (3 + 3 + 2), 10 (3 + 3 + 3 + 1), 13 (3 + 3 + 3 + 3 + 1). So, the sum of count of each element is (2+3+4+5)=14.

==========================================================================================================


class Solution {
    int totalCount(int k, int[] arr) {
        // code here
         int total = 0; // to store the total count of integers
        
        for (int x : arr) {
            // Full parts of k
            total += x / k;
            // If there's a remainder, add one more
            if (x % k > 0) {
                total++;
            }
        }
        
        return total;
    }
}
