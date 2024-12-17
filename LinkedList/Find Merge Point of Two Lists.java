public static int findMergeNode(SinglyLinkedListNode head1, SinglyLinkedListNode head2) {
        SinglyLinkedListNode ptr1 = head1;
        SinglyLinkedListNode ptr2 = head2;

        // Traverse both lists until they meet
        while (ptr1 != ptr2) {
            // If ptr1 reaches the end of its list, start at head2
            ptr1 = (ptr1 == null) ? head2 : ptr1.next;
            // If ptr2 reaches the end of its list, start at head1
            ptr2 = (ptr2 == null) ? head1 : ptr2.next;
        }

        // At this point, ptr1 and ptr2 point to the merge node
        return ptr1.data;
    }
============================================

If a pointer reaches the end of a list, it is reset to the head of the other list.
This ensures both pointers traverse an equal total distance before meeting at the merge point.

Time Complexity: O(m + n)
Space Complexity: O(1)
