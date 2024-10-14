class Solution {
    public void traversal(TreeNode root, List<Integer> res){
        if (root != null){
            traversal(root.left, res);
            traversal(root.right, res);
            res.add(root.val);
        }
    }

    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        traversal(root, res);
        return res;
    }
}

==========================================================

Input: root = [1,null,2,3]

Output: [3,2,1]

Example 2:

Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

Output: [4,6,7,5,2,9,8,3,1]
