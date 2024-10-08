class Solution:
    def pairsum(self, arr: list[int]) -> int:
        # Initialize two variables to store the largest and second largest
        largest = second_largest = float('-inf')

        # Traverse the array once
        for num in arr:
            if num > largest:
                second_largest = largest  # Update second largest
                largest = num  # Update largest
            elif num > second_largest:
                second_largest = num  # Update second largest if the current number is less than largest but greater than second largest

        # Return the sum of the largest and second largest elements
        return largest + second_largest
==========================================================================================

Find the largest pair sum in an array of distinct integers.

Examples :

Input: arr[] = [12, 34, 10, 6, 40]
Output: 74
Explanation: Sum of 34 and 40 is the largest, i.e, 34 + 40 = 74.
Input: arr[] = [10, 20, 30]
Output: 50
Explanation: 20 + 30 = 50.
