class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class BST:
    def addNode(self,root,value):
        newNode = Node(value)
        if root==None:
            return newNode
        else:
            if value<root.data:
                if root.left==None:
                    root.left=newNode
                else:
                    self.addNode(root.left,value)
            # if value>=root.data:
            else:
                if root.right==None:
                    root.right=newNode
                else:
                    self.addNode(root.right,value)

    def inOrder(self,root):
        if root.left!=None:
            self.inOrder(root.left)
        print(root.data,end=',')
        if root.right!=None:
            self.inOrder(root.right)
    def preOrder(self,root):
        pass
    def postOrder(self,root):
        pass
    def levelOrder(self,root):
        pass

tree=BST()
root=None
values=[15,6,56,22,5,3,66,3]
root=tree.addNode(root,values[0])
for i in range(1,len(values)):
    tree.addNode(root,values[i])
tree.inOrder(root)