class Solution:
    def twoOddNum(self, Arr, N):
        bitMask = 0
        for ele in Arr:
            bitMask = bitMask ^ ele
        actualSeperator = (bitMask & (bitMask - 1)) ^ bitMask 
        bucket1, bucket2 = 0, 0
        for ele in Arr:
            if ele & actualSeperator: 
                bucket1 =  bucket1 ^ ele
            else: 
                bucket2 =  bucket2 ^ ele
        result = [bucketi, bucket2] 
        if result[0] <result[1]: 
            result[0], result[1] = result[1], result[0]
        return result