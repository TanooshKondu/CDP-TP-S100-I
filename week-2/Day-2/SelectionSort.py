#https://pastebin.com/Lrw4A3Q5

def SelectionSort(nums):
    n = len(nums)
    Pos = n-1
    
    while Pos > 0:
        ele = Pos
        for index in range(0, Pos-1):
            if nums[ele] < nums[index]:
                ele = index
            if ele != Pos:
                temp = nums[ele]
                nums[ele] = nums[Pos]
                nums[Pos] = temp
        Pos -= 1
            
#nums = [9, 8, 7, 6, 5, 4, 3, 2, 10]
#SelectionSort(nums)
#print(nums)


#sir code --->>>>>>>>>
def performSelectionSort(nums, n):
    if n == 1:
        return 
 
    # fix (n-1)th index 
    maxEleIndex = n - 1 
    for index in range(n - 1):
        if nums[index] > nums[maxEleIndex]:
            maxEleIndex = index 
 
    if maxEleIndex != n - 1:
        nums[maxEleIndex], nums[n - 1] = nums[n - 1], nums[maxEleIndex]
 
    performSelectionSort(nums, n - 1)
nums = [8, 1, 7, 6, 5, 4, 3, 2]

print("Before sorting:", nums)
performSelectionSort(nums, len(nums))
print("After sorting:", nums)

