----<=>---Iterative:

  class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m = len(word1)
        n = len(word2)
        s = ''
        i = 0
        j = 0 
        while(i < m and j < n):
            s += word1[i]
            s += word2[j]
            i+=1
            j+=1
        if i < m : s += word1[i:]
        if j < n : s += word2[j:]
        return s

----<=>---Recursive:

    class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        if not word2: return word1

        if not word1: return word2

        return word1[0] + mergeAlternately(word2, word1[1:])


======================
The (iterative) is much more efficient than the first one:
Time Complexity: The iterative approach runs in O(m + n), while the recursive one has O((m + n)^2) due to repeated slicing.
Space Complexity: The iterative version only requires space for the final result string, while the recursive one also uses space for the recursion stack and intermediate sliced strings.
