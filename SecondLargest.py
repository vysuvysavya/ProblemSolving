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
---------------------------------------------------------
class Solution:
    def getSecondLargest(self, arr):
        # Remove duplicates and sort in descending order
        arr = list(set(arr))
        if len(arr) < 2:
            return -1  # Return -1 if there's no second largest
        arr.sort(reverse=True)
        return arr[1]  # Return the second largest element
