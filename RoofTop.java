You are given the heights of consecutive buildings. You can move from the roof of a building to the roof of the next adjacent building. 
You need to find the maximum number of consecutive steps you can put forward such that you gain an increase in altitude with each step.

Examples:

Input: arr[] = [1, 2, 2, 3, 2]
Output: 1
Explanation: 1, 2, or 2, 3 are the only consecutive buildings with increasing heights thus maximum number of consecutive steps with an increase in gain in altitude would be 1 in both cases.
Input: arr[] = [1, 2, 3, 4]
Output: 3
Explanation: 1 to 2 to 3 to 4 is the jump of length 3 to have a maximum number of buildings with increasing heights, so maximum steps with increasing altitude becomes 3.
===============================

class Solution {
    // Function to find maximum number of consecutive steps
    // to gain an increase in altitude with each step.
    public int maxStep(int arr[]) {
        // Your code here
         int maxSteps = 0; // To keep track of maximum steps
        int currentSteps = 0; // To count the current consecutive steps
        
        for (int i = 1; i < arr.length; i++) {
            // Check if the current building is taller than the previous one
            if (arr[i] > arr[i - 1]) {
                currentSteps++; // Increment the count of current steps
            } else {
                // Reset current steps if no increase
                currentSteps = 0;
            }
            // Update maxSteps if currentSteps is greater
            maxSteps = Math.max(maxSteps, currentSteps);
        }
        
        return maxSteps;
    }
}
