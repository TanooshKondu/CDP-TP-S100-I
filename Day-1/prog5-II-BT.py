##find 1.sum, 2.max, 3.min, 4.minEven, 5.maxEven in the list using recursion\//12, 34, 12, 5, 7
#USING BACKTRACKING SUM, MAX, MIN

def prog(index, n, nums,result, max1, min1):
    if index == n:
        print(result)
        print(max1)
        print(min1)
        return
    result += nums[index]
    if max1 < nums[index]:
        max1= nums[index]
    if min1 > nums[index]:
        min1 = nums[index]
    prog(index+1, n, nums,result, max1, min1)
index = 0
nums = list(map(int, input().split(",")))
n = len(nums)
max1 = nums[index]
min1 = nums[index]
result = 0
prog(0, n, nums,result, max1, min1)