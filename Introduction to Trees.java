class Solution {
    static int countNodes(int i) {
        return (int) Math.pow(2, i - 1);
    }
}
====================
Introduction to Trees
Difficulty: EasyAccuracy: 82.66%Submissions: 48K+Points: 2Average Time: 15m
Given an integer i. Print the maximum number of nodes on level i of a binary tree.

Example 1:

Input: 5
Output: 16
Example 2:

Input: 1
Output: 1
