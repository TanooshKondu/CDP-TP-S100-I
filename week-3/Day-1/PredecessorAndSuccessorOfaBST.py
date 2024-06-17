#gfg
class Solution:
    def findPreSuc(self, root, pre, suc, key):

        def helper(currNode):
            if not currNode:
                return 
            elif currNode.key == key:
                # Predecessor
                temp = currNode.left 
                while temp and temp.right:
                    temp = temp.right 
                if temp:
                    pre.key = temp.key 

                # Successor
                temp = currNode.right 
                while temp and temp.left:
                    temp = temp.left 

                if temp:
                    suc.key = temp.key

                return
            elif currNode.key > key:
                suc.key = currNode.key 
                helper(currNode.left)
            else:
                pre.key = currNode.key
                helper(currNode.right)
        helper(root)
