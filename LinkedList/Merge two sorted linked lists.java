
class Solution {
    Node sortedMerge(Node head1, Node head2) {
        // code here
        Node dummy = new Node(-1);
        Node temp = dummy;
        Node t1 = head1;
        Node t2 = head2;
        
        while(t1!=null && t2 != null){
            if (t1.data<t2.data){
                temp.next = t1;
                t1= t1.next;
            }
            else{
                temp.next = t2;
                t2 = t2.next;
            }
            temp = temp.next;
        }
        if (t1!=null) temp.next = t1;
        if (t2!=null) temp.next = t2;
        return dummy.next;
    }
}

===================

Input: head1 = 5 -> 10 -> 15 -> 40, head2 = 2 -> 3 -> 20
Output: 2 -> 3 -> 5 -> 10 -> 15 -> 20 -> 40
