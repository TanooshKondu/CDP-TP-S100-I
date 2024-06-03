##find 1.sum, 2.max, 3.min, 4.minEven, 5.maxEven in the list using recursion\//12, 34, 12, 5, 7
#https://pastebin.com/fZiLtTAF
#using Dynamic Programming
# Passing data from child function to Parent function
def progMax(index, n, nums):
    if index == n-1:
        return nums[index]
    nextMax = progMax(index+1, n, nums)
    if nums[index] > nextMax:
        return nums[index]
    else:
        return nextMax
    
index = 0
nums = [12, 34, 12, 5, 7]
n = len(nums)
result = progMax(0, n, nums)
print("max is: ", result)
