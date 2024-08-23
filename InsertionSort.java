class Solution
{
    // Function to insert element at index i into its correct position
    static void insert(int arr[], int i)
    {
        int key = arr[i];
        int j = i-1;
        // Move elements of arr[0..i-1], that are greater than key,
        // to one position ahead of their current position
        while (j >= 0 && arr[j] >= key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j+1] = key;
    }

    // Function to sort the array using insertion sort algorithm.
    public void insertionSort(int arr[], int n)
    {
        for (int i = 1; i < n; i++) {
            // Insert arr[i] into its correct position in the sorted part of the array
            insert(arr, i);
        }
    }
}

Time complexity: O(N2), (where N = size of the array), for the worst, and average cases.
time complexity in the best case will boil down to O(N)
