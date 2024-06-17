#https://pastebin.com/ciDzSe36

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def printBoundaryView(self, root):

        result = []
        if not root:
            return result

        if root.left or root.right:
            result.append(root.data)

        def collectLeftView(root):
            while root:
                if root.left == None and root.right == None:
                    break
                result.append(root.data)
                if root.left != None:
                    root = root.left 
                else:
                    root = root.right

        def collectLeafNodes(root):
            # pre-order 
            if not root:
                return 

            if root.left == None and root.right == None:
                result.append(root.data)
                return 
            collectLeafNodes(root.left)
            collectLeafNodes(root.right)

        def collectRightView(root):
            temp = []

            while root != None:
                if root.left == None and root.right == None:
                    break
                temp.append(root.data)
                if root.right:
                    root = root.right 
                else:
                    root = root.left

            # reversing the temp 
            # adding all those elements one by one to result
            result.extend(temp[::-1])

        # step-1 collect left view 
        collectLeftView(root.left)

        # step-2 collect leaf nodes  (left to right direction)
        collectLeafNodes(root)

        # step-3 collect right view (in reverse direction)
        collectRightView(root.right)

        return result
