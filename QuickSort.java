class Solution
{
    //Function to sort an array using quick sort algorithm.
    static void quickSort(int arr[], int low, int high)
    {
        // code here
        if(low<high){
            int partition = partition(arr,low,high);
            quickSort(arr, low,partition-1);
            quickSort(arr, partition+1 , high);
            
        }
    }
    static int partition(int arr[], int low, int high)
    {
        // your code here
        int pivot = arr[low];
        int i = low, j = high;
        while(i<j){
            while(arr[i]<=pivot && i<high) i++;
            while(arr[j]>=pivot && j>low) j--;
            if (i<j) {
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
        int temp = arr[low];
        arr[low] = arr[j];
        arr[j] = temp;
        return j;
    } 
}

Time Complexity: O(N*logN), where N = size of the array.

Reason: At each step, we divide the whole array, for that logN and n steps are taken for partition() function, so overall time complexity will be N*logN.

Worst Case Time complexity: O(n2) 


