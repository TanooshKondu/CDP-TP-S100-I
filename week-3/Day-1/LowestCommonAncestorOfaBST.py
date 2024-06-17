#LeEtcode-235
#https://pastebin.com/1PyXQwGr

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return None 

        currNode = root 
        while currNode:
            if currNode.val > p.val and currNode.val > q.val:
                currNode = currNode.left 
            elif currNode.val < p.val and currNode.val < q.val:
                currNode = currNode.right 
            else:
                return currNode 
        return None
