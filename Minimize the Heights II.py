class Solution:
    def getMinDiff(self, arr, k):
        n = len(arr)
        if n == 1:
            return 0
        
        # Sort the array
        arr.sort()
        
        # Initial difference between the maximum and minimum
        result = arr[-1] - arr[0]
        
        # Traverse through the array and try minimizing the difference
        for i in range(1, n):
            if arr[i] >= k:
                # Maximum possible height after decreasing the tallest
                max_height = max(arr[i-1] + k, arr[-1] - k)
                # Minimum possible height after increasing the shortest
                min_height = min(arr[0] + k, arr[i] - k)
                result = min(result, max_height - min_height)
        
        return result
=============================================================================================================

Given an array arr[] denoting heights of N towers and a positive integer K.

For each tower, you must perform exactly one of the following operations exactly once.

Increase the height of the tower by K
Decrease the height of the tower by K
Find out the minimum possible difference between the height of the shortest and tallest towers after you have modified each tower.

Note: It is compulsory to increase or decrease the height by K for each tower. After the operation, the resultant array should not contain any negative integers.

Examples :

Input: k = 2, arr[] = {1, 5, 8, 10}
Output: 5
Explanation: The array can be modified as {1+k, 5-k, 8-k, 10-k} = {3, 3, 6, 8}.The difference between the largest and the smallest is 8-3 = 5.
Input: k = 3, arr[] = {3, 9, 12, 16, 20}
Output: 11
Explanation: The array can be modified as {3+k, 9+k, 12-k, 16-k, 20-k} -> {6, 12, 9, 13, 17}.The difference between the largest and the smallest is 17-6 = 11. 
Expected Time Complexity: O(n*logn)
Expected Auxiliary Space: O(n)

====================================================================================================


1. Sort the Array:
Sorting the array helps in easily identifying the smallest and largest elements, which are crucial in minimizing the difference.

2. Modify the Extremes (Smallest and Largest Towers):
The main idea is to either increase the smaller towers (towards the start of the array) or decrease the larger towers (towards the end).
This way, you bring the extremes (smallest and largest) closer together, which helps minimize the difference between the tallest and shortest towers.

3. Evaluate Both Sides:
For each tower, consider both possibilities:

Decrease the current tallest tower.
Increase a previous shorter tower. This comparison ensures that you are balancing the adjustments to the array effectively, allowing you to achieve the minimum difference.
4. Focus on Maximum and Minimum Heights:
After sorting and applying the operations, always track:

The new maximum height, which can come from either the decreased largest element or an increased smaller element.
The new minimum height, which can come from either an increased smallest element or a decreased larger element.
5. Optimize the Height Difference:
The essence of the problem is to adjust the heights in such a way that the range (difference) between the highest and lowest towers becomes as small as possible. 
This is achieved by selectively modifying the extreme values in the array.

Core Logic to Remember:
Always think about manipulating the boundary elements (smallest and largest) rather than focusing on every single element.
Compare options to increase and decrease carefully for each tower, especially when modifying the largest and smallest towers.
Sort the array first to make these comparisons and operations easier to implement.
