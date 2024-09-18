Input: {([])}
Output: true
Explanation: { ( [ ] ) }. Same colored brackets can form balanced pairs, with 0 number of unbalanced bracket.
Input: ()
Output: true
Explanation: (). Same bracket can form balanced pairs,and here only 1 type of bracket is present and in balanced way.
Input: ([]
Output: false
Explanation: ([]. Here square bracket is balanced but the small bracket is not balanced and Hence , the output will be unbalanced
==========================================================================================================================================


class Solution:
    
    #Function to check if brackets are balanced or not.
    def ispar(self,x):
        # code here
        st = []
        for i in x:
            if i == '[' : st+= ']'
            elif i == '(' : st += ')' 
            elif i == '{' : st += '}'
            elif len(st)==0  or st.pop() != i  : return False
        return len(st)==0
