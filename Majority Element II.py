You are given an array of integer arr[] where each number represents a vote to a candidate. Return the candidates that have votes greater than one-third of the total votes, If there's not a majority vote, return an empty array. 

Note: The answer should be returned in an increasing format.

Examples:

Input: arr[] = [2, 1, 5, 5, 5, 5, 6, 6, 6, 6, 6]
Output: [5, 6]
Explanation: 5 and 6 occur more n/3 times.
Input: arr[] = [1, 2, 3, 4, 5]
Output: []
Explanation: no candidate occur more than n/3 times.
===================================================

class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        #Your Code goes here.
        d = {}
        for i in arr:
            if i in d: d[i]+=1
            else : d[i]=1
        x = len(arr)//3
        res = [i for i in d if d[i]>x]
        return sorted(res)

=================================================

or in alternate way using built-in methods
 # Function to find the majority elements in the array
    def findMajority(self, arr):
        # Dictionary to count occurrences of each number
        count = {}
        for num in arr:
            count[num] = count.get(num, 0) + 1
        
        # Calculate the threshold for majority
        threshold = len(arr) // 3
        
        # Find all candidates that appear more than threshold times
        result = [key for key, value in count.items() if value > threshold]
        
        # Return the result in sorted order
        return sorted(result)

============================================================
Boyer-Moore Majority Vote Algorithm

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        majority1 = majority2 = count1 = count2 = 0

        for num in nums:
            if num == majority1:
                count1 += 1
            elif num == majority2:
                count2 += 1
            elif count1 == 0:
                majority1 = num
                count1 += 1
            elif count2 == 0:
                majority2 = num
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        count1, count2 = 0, 0
        for num in nums:
            if num == majority1:
                count1 += 1
            elif num == majority2:
                count2 += 1
        res = []
        if count1 > len(nums) // 3:
            res.append(majority1)
        if count2 > len(nums) // 3:
            res.append(majority2)
        return res
