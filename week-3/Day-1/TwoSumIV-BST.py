#leetcode-653
#https://pastebin.com/fmeG4LgN

class Solution(object):
    def findTarget(self, root, k):
        visited = set()
 
        def helper(currNode):
            if not currNode:
                return False 
 
            otherEle = k - currNode.val 
            if otherEle in visited:
                return True 
            visited.add(currNode.val)
            leftSubtree = helper(currNode.left)
            rightSubtree = helper(currNode.right)
            return leftSubtree or rightSubtree
        return helper(root)
