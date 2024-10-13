class Solution {
    public void deleteAlt(Node head) {
        // Code Here
        if (head== null) return;
        Node temp = head;
        while(temp!=null && temp.next!= null){
            temp.next = temp.next.next;
            temp = temp.next;
        }
    }
}

===============================

Input: LinkedList: 1->2->3->4->5->6
 
Output: 1->3->5

Explanation: Deleting alternate nodes ie 2, 4, 6 results in the linked list with elements 1->3->5.
Input: LinkedList: 99->59->42->20
 
Output: 99->42
 
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)
