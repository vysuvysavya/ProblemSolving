
class Solution {
    int height(Node node) {
        if (node == null) return -1;
        int leftHeight = height(node.left);
        int rightHeight = height(node.right);
        return Math.max(leftHeight, rightHeight) + 1;
    }
}
