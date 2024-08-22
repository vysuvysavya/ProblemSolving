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