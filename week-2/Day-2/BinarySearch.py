def BinarySearch(nums,target,n,found,left,right): 
    n = len(nums)
    if left <= right:
        mid = (left + right) // 2 
        if nums[mid] == target:
            return True 
        elif nums[mid] < target:
            return BinarySearch(nums,target,n,found,mid+1,right)
        else:
            return BinarySearch(nums, target, n, found,left,mid-1)
    
            
nums = [12, 34, 21, 23, 44, 56];
target = 23
nums = sorted(nums)

BinarySearch(nums,target,len(nums),False,0,len(nums)-1)
found = False
if  True:
    print("Target found")
else:
    print("Target Not found")


