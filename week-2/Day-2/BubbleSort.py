def BubbleSort(nums):
    n = len(nums)
    pos = n-1
    
    while pos > 0:
        for i in range(pos):
            if nums[i] > nums[i+1]:
                nums[i],nums[i+1] = nums[i+1], nums[i]
        return nums
        pos -= 1
    
nums = [1, 4, 2, 16]
print(BubbleSort(nums))