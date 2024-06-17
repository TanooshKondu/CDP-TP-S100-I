#https://pastebin.com/Bt5fCwPp

class Solution(object):
    def isValidBST(self, root):
 
        # For Earlier Approach:
        # TC --> O(N)
        # SC --> O(N) (Because of that inorder list)
 
        # For This Approach:
        # TC --> O(N)
        # SC --> O(1) (Because we are not using inorder list)
 
 
        previous = [None]
 
        def findInorder(root):
            if not root:
                return True
 
            checkLeft = findInorder(root.left)
            if not checkLeft:
                return False
 
            if previous[0] and previous[0].val >= root.val:
                return False
            previous[0] = root
 
            checkRight = findInorder(root.right)
            if not checkRight:
                return False
            return True
 
        return findInorder(root)
 
