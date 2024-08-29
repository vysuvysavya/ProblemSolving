class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int n = nums.length;
        int currentcount = 0;
        int maxcount = 0;

        for(int i=0;i<n;i++){
            if(nums[i]==1){
                currentcount++;
            }
            else{
                if(currentcount>maxcount){
                    maxcount=currentcount;
                }
                currentcount=0;
            }
        }
        if(currentcount>maxcount){
            maxcount=currentcount;
        }
        return maxcount;


    }
}


Input: nums = [1,1,0,1,1,1]
Output: 3
