#LEETCODE-703

#https://pastebin.com/fnTMQkyv

class KthLargest(object):
     
    def __init__(self, k, nums):
        self.minHeap = []
        self.k = k
        heapify(self.minHeap)
 
        for ele in nums:
            heappush(self.minHeap, ele)
            if len(self.minHeap) > k:
                heappop(self.minHeap)
 
    def add(self, val):
        heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heappop(self.minHeap)
        return self.minHeap[0]