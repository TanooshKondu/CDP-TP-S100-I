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
            
nums = [9, 8, 7, 6, 5, 4, 3, 2, 10]
SelectionSort(nums)
print(nums)


#def SelectionSortRecc(nums, index)