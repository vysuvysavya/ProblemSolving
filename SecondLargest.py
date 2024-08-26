class Solution:
    def print2largest(self, arr):
        first_largest = second_largest = -1
        
        for i in range(len(arr)):
            if arr[i] > first_largest:
                second_largest = first_largest
                first_largest = arr[i]
            elif arr[i] > second_largest and arr[i] != first_largest:
                second_largest = arr[i]
        
        return second_largest
-----------------------------------------------------------------------------

Input: arr = [12, 35, 1, 10, 34, 1]
Output: 34
