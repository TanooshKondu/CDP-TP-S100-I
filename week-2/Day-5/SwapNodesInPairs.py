#https://hastebin.com/share/vuzuhodima.python
#LEETCODE - 24


class Solution(object):
    def swapPairs(self, head):
        if not head or not head.next:
            return head 

        dummyNode = ListNode(-1)
        tail = dummyNode 
        curr = head 
        while curr and curr.next:
            storeNext = curr.next.next 
            curr.next.next = curr 
            tail.next = curr.next 
            tail = curr 
            curr = storeNext 
        if curr:
            tail.next = curr 
        else:
            tail.next = None


        return dummyNode.next
