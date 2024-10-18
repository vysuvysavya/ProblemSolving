Given a sorted array arr[] of size n without duplicates, and given a value x.
    Floor of x is defined as the largest element k in arr[] such that k is smaller than or equal to x. Find the index of k(0-based indexing).

Examples

Input: n = 7, x = 0 arr[] = {1,2,8,10,11,12,19}
Output: -1
Explanation: No element less than 0 is found. So output is "-1".
Input: n = 7, x = 5 arr[] = {1,2,8,10,11,12,19}
Output: 1
Explanation: Largest Number less than 5 is 2 (i.e k = 2), whose index is 1(0-based indexing).

==============================================================
class Solution {

    // Function to find floor of x
    static int findFloor(long arr[], int n, long x) {
        int low = 0;
        int high = n - 1;
        int result = -1;
        
        // Perform binary search
        while (low <= high) {
            int mid = low + (high - low) / 2;
            
            // If arr[mid] is smaller than or equal to x, it's a potential answer
            if (arr[mid] <= x) {
                result = mid; // Store the index of current floor candidate
                low = mid + 1; // Search in the right half for a better candidate
            } else {
                high = mid - 1; // Search in the left half
            }
        }
        
        return result; // Return the index of the floor of x or -1 if no such floor exists
    }
}
