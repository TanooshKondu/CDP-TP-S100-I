#https://hastebin.com/share/ijiwaqabow.python
#LEETCODE-25

class Solution(object):
    def reverseKGroup(self, head, k):
        length = 0 
        curr = head 
        while curr:
            curr = curr.next 
            length += 1 

        def doReverse(head):
            prev, curr = None, head 
            while curr:
                next = curr.next 
                curr.next = prev 
                prev = curr 
                curr = next 
            return prev

        mainHead, tail = None, None 
        curr = head 
        while length >= k:
            temp = curr 
            prev = None
            for i in range(k):
                prev = curr 
                curr = curr.next
            prev.next = None 
            revHead = doReverse(temp)
            if mainHead == None:
                mainHead = revHead 
                tail = temp
            else:
                tail.next = revHead
                tail = temp 
            length -= k 
        tail.next = curr
        return mainHead
