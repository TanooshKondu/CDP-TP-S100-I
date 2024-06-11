#https://pastebin.com/Lrw4A3Q5

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
#nums = [1, 4, 2, 16]
#BubbleSortRecc(nums,0,1)
#print(nums)

##sir code----->>>>>>>>>>
def performBubbleSort(nums, n):
    if n == 1:
        return 
    # last index is (n - 1)
    for index in range(n - 1):
        if nums[index] > nums[index + 1]:
            nums[index], nums[index + 1] = nums[index + 1], nums[index]
 
    performBubbleSort(nums, n - 1)    
nums = [8, 1, 7, 6, 5, 4, 3, 2]

print("Before sorting:", nums)
performBubbleSort(nums, len(nums))
print("After sorting:", nums)