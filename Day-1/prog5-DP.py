##find 1.sum, 2.max, 3.min, 4.minEven, 5.maxEven in the list using recursion\//12, 34, 12, 5, 7
#https://pastebin.com/fZiLtTAF
#using Dynamic Programming
# Passing data from child function to Parent function
def prog(index, n, nums):
    if index == n:
        return 0
    nextElementSum = prog(index +1, n, nums)
    return nextElementSum + nums[index]
nums = list(map(int,input().split(",")))
n = len(nums)
result = prog(0, n, nums)
print("sum is: ", result)
