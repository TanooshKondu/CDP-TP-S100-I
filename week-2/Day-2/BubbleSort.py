def BubbleSort(nums):
    n = len(nums)
    pos = n-1
    
    while pos > 0:
        for i in range(pos):
            if nums[i] > nums[i+1]:
                nums[i],nums[i+1] = nums[i+1], nums[i]
        return nums
        pos -= 1
    
#nums = [1, 4, 2, 16]
#print(BubbleSort(nums))


def BubbleSortRecc(nums,index1,index2):
    n = len(nums)
    if index1 == n or index2 == n:
        return 
    if nums[index1]> nums[index2]:
        nums[index1], nums[index2] = nums[index2], nums[index1]
    return BubbleSortRecc(nums, index1+1, index2+1)
nums = [1, 4, 2, 16]
BubbleSortRecc(nums,0,1)
print(nums)