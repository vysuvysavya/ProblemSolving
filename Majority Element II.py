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
