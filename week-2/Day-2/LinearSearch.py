def LinearSearch(nums,index,target,n):
    n = len(nums)
    if index == n:
        return -1
    elif nums[index] == target:
        return index 
    return LinearSearch(nums,index+1, target, n)
    
nums = [12, 34, 21, 23, 44, 56];
target = 23 
index = LinearSearch(nums,0,target, len(nums))
if index == -1:
    print(target, "not found")
else:
    print(target, "found at index:", index)

