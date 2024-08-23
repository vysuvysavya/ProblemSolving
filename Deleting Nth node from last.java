/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
--brute force 
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
       int l=0;

       if (head.next==null) return head.next;
       
       ListNode temp = head;
       while(temp!=null){
        l++;
        temp=temp.next;
       } 
       if(l==n){
        head = head.next;
        return head;
       }

       int x = l-n-1;
       int c = 0;
       temp = head;
       while(c!=x){
            temp = temp.next;
            c++;
       }
        if (c==x){
            temp.next = temp.next.next;
        }
        return head;
    }
}
Time Complexity: O(L)+O(L-N), We are calculating the length of the linked list and then iterating up to the (L-N)th node of the linked list, where L is the total length of the list.

--optimal 

 ListNode f=head,s=head;
       for(int i = 1;i<=n; i++) f = f.next;
       if (f == null) return head.next;  
       while(f.next!=null) {
        s = s.next;
        f = f.next;
       }
       s.next = s.next.next;
       return head;

Time Complexity: O(N)
