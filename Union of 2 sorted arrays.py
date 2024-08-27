Given two sorted arrays of size n and m respectively, find their union. The Union of two arrays can be defined as the common and distinct elements in the two arrays. Return the elements in sorted order.

Example 1:

Input: 
n = 5, arr1[] = {1, 2, 3, 4, 5}  
m = 5, arr2 [] = {1, 2, 3, 6, 7}
Output: 
1 2 3 4 5 6 7
  
========================================================================================================

class Solution:
    
    def findUnion(self, arr1, arr2, n, m):
        result = []
        i, j = 0, 0
        
        while i < n and j < m:
            # If the current element of arr1[] is smaller, add it
            if arr1[i] < arr2[j]:
                if len(result) == 0 or result[-1] != arr1[i]:
                    result.append(arr1[i])
                i += 1
            # If the current element of arr2[] is smaller, add it
            elif arr1[i] > arr2[j]:
                if len(result) == 0 or result[-1] != arr2[j]:
                    result.append(arr2[j])
                j += 1
            # If both elements are the same, add it once
            else:
                if len(result) == 0 or result[-1] != arr1[i]:
                    result.append(arr1[i])
                i += 1
                j += 1
        
        # Add remaining elements of arr1[]
        while i < n:
            if len(result) == 0 or result[-1] != arr1[i]:
                result.append(arr1[i])
            i += 1
        
        # Add remaining elements of arr2[]
        while j < m:
            if len(result) == 0 or result[-1] != arr2[j]:
                result.append(arr2[j])
            j += 1
        
        return result
