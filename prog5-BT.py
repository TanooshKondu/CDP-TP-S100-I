##find 1.sum, 2.max, 3.min, 4.minEven, 5.maxEven in the list using recursion\//12, 34, 12, 5, 7
#https://pastebin.com/fZiLtTAF
#using backtracking

def prog5(index, n, nums, result):
    if index == n:
        print("Sun is: ", result)
        return
    result += nums[index]
    prog5(index+1, n, nums, result)
    
nums = list(map(int, input().split(",")))
n = len(nums)
prog5(0, n, nums,0)