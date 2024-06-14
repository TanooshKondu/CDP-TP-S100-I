#206-LEETCODE

#https://hastebin.com/share/ajakehagiv.python
#RECURSIVE CODE
class Solution(object):
    def reverseList(self, head):
        if not head or not head.next:
            return head
        reversedHead = [None] 

        def helper(head):
            if not head.next:
                reversedHead[0] = head
                return head 
            tailNode = helper(head.next)
            tailNode.next = head 
            return head


        tailNode = helper(head)
        tailNode.next = None
        return reversedHead[0]