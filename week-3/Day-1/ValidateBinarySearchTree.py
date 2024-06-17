#LEETCODE-98
#https://pastebin.com/59snHyit

class Solution(object):
    def isValidBST(self, root):
        inorder = []

        def findInorder(root):
            if not root:
                return 

            findInorder(root.left)
            inorder.append(root.val)
            findInorder(root.right)

        findInorder(root)
        for index in range(1, len(inorder)):
            if inorder[index] <= inorder[index - 1]:
                return False 
        return True
