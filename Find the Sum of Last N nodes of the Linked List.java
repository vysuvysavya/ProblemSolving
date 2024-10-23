
class Solution {

    // Return the sum of last k nodes
    public int sumOfLastN_Nodes(Node head, int n) {
        // write code here
        Node temp = head;
        int l = 0;
        while(temp!= null){
            l +=1 ;
            temp = temp.next;
        }
        int x = l - n + 1;
        int s = 0, cc = 1;
        temp = head;
        while(temp!=null){
            if (cc>=x){
            s += temp.data;
            }
                        temp = temp.next;
                        cc +=1;
        }
        return s;
    }
}

==========================================================

Given a single linked list, calculate the sum of the last n nodes.

Note: It is guaranteed that n <= number of nodes.

Examples:

Input: Linked List: 5->9->6->3->4->10, n = 3

Output: 17
Explanation: The sum of the last three nodes in the linked list is 3 + 4 + 10 = 17.
Input: Linked List: 1->2, n = 2

Output: 3
Explanation: The sum of the last two nodes in the linked list is 2 + 1 = 3.
