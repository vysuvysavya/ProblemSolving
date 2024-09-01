
/*Complete the function below*/
class GfG {
    public Stack<Integer> sort(Stack<Integer> s) {
        // Base case: if the stack is empty
        if (s.isEmpty()) {
            return s;
        }
        
        // Step 1: Pop the top element
        int top = s.pop();
        
        // Step 2: Recursively sort the remaining stack
        sort(s);
        
        // Step 3: Insert the top element back in sorted order
        insertInSortedOrder(s, top);
        
        return s;
    }

    // Helper function to insert an element into the sorted stack
    private void insertInSortedOrder(Stack<Integer> s, int element) {
        // Base case: if the stack is empty or the top of the stack is less than the element
        if (s.isEmpty() || s.peek() < element) {
            s.push(element);
            return;
        }
        
        // If the current element is smaller, pop the top element
        int top = s.pop();
        
        // Recur to insert the element in the correct position
        insertInSortedOrder(s, element);
        
        // Push the popped element back into the stack
        s.push(top);
    }
}


=====================================================================================================================================

Expected Time Complexity: O(N*N)
Expected Auxilliary Space: O(N) recursive.
