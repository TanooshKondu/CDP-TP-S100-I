#MIN HEAP

from heapq import heapify, heappush, heappop

minHeap = []
heapify(minHeap)

nums = [23, 31, 11, 24, 4]

for ele in nums:
    heappush(minHeap, -1*ele)
    
while minHeap:
    