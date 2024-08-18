class Solution {
    public boolean canSplit(int arr[]) {
        int totalSum = 0;

        // Calculate the total sum of the array
        for (int num : arr) {
            totalSum += num;
        }

        // If the total sum is odd, we can't split it into two equal parts
        if (totalSum % 2 != 0) {
            return false;
        }

        int halfSum = totalSum / 2;
        int prefixSum = 0;

        // Iterate through the array and calculate prefix sums
        for (int num : arr) {
            prefixSum += num;

            // If prefix sum equals half of the total sum, we found the split point
            if (prefixSum == halfSum) {
                return true;
            }
        }

        // If no such point is found, return false
        return false;
    }
}
