#leetcode-230

#https://pastebin.com/JvR8vHi6
class Solution:
    def kthLargest(self,root, k):
        # Since below 2 lists size is not dependent on N, so we can say that 
        # Space complexity is O(1)
        # Time complexit is O(N)
        value = [k]
        result = [-1]

        def collectInorderTraversal(currNode):
            if not currNode:
                return 

            collectInorderTraversal(currNode.right)
            value[0] -= 1 
            if value[0] == 0:
                result[0] = currNode.data 

            collectInorderTraversal(currNode.left)

        collectInorderTraversal(root)
        return result[0]
