class Solution {
    public void rotate(int[] nums, int k) {
        k %= nums.length;
        reverse(nums, 0, nums.length-1);
        reverse(nums, 0, k-1);
        reverse(nums, k, nums.length-1);
    }

    public void reverse(int[] nums, int start, int end){
        while(start < end){
            int temp = nums[start];
            nums[start] = nums[end];
            nums[end] = temp;
            start++;
            end--;
        }
    }
}
===========================================================================================================================
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 class Solution:
    # Function to rotate an array by d elements in counter-clockwise direction.
    def rotateArr(self, arr, d):
        n = len(arr)
        d %= n  # To handle cases where d > n
        # Reverse the first d elements
        self.reverse(arr, 0, d - 1)
        # Reverse the remaining elements
        self.reverse(arr, d, n - 1)
        # Reverse the entire array
        self.reverse(arr, 0, n - 1)
    
    # Helper function to reverse elements in the array between two indices
    def reverse(self, arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]

