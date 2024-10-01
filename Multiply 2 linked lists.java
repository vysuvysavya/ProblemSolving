Given elements as nodes of the two singly linked lists. The task is to multiply these two linked lists, say L1 and L2.

Note: The output could be large take modulo 109+7.

Examples :

Input: LinkedList L1 : 3->2 , LinkedList L2 : 2
Output: 64
Explanation: 

Multiplication of 32 and 2 gives 64.
=======================================================================================================================

 public long multiplyTwoLists(Node first, Node second) {
        // Convert the first linked list to a number
        long num1 = 0;
        long num2 = 0;

        // Traverse the first linked list and construct the number
        while (first != null) {
            num1 = (num1 * 10 + first.data) % MOD;
            first = first.next;
        }

        // Traverse the second linked list and construct the number
        while (second != null) {
            num2 = (num2 * 10 + second.data) % MOD;
            second = second.next;
        }

        // Multiply the two numbers and take modulo
        return (num1 * num2) % MOD;
    }
