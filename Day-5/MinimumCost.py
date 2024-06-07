#https://pastebin.com/048fdZYK

#LEETCODE 746

class Solution(object):
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        cache = [-1] * n
        def solveIt(index, n, cost):
            if index >= n:
                return 0 
            elif cache[index] != -1:
                return cache[index]
            jump1 = solveIt(index + 1, n, cost)
            jump2 = solveIt(index + 2, n, cost)
            cache[index] = min(jump1, jump2) + cost[index]
            return cache[index]
 
 
        def solveItUsingTabulation(cost):
            cache = [-1] * (n + 2)
            cache[n] = 0
            cache[n + 1] = 0 
            for index in range(n - 1, -1, -1):
                jump1 = cache[index + 1]
                jump2 = cache[index + 2]
                cache[index] = min(jump1, jump2) + cost[index]
            return min(cache[0], cache[1])
 
        return solveItUsingTabulation(cost)
 
        # option1 = solveIt(0, n, cost)
        # option2 = solveIt(1, n, cost)
        # return min(option1, option2)
        
#LEETCODE - 198        
#using recursion find if str is palindrome or not
#check whether 2 str's same or not
#Check whether one string is a subsequence of the other or not using recursion.
#Starting from (n-1, n-1), reach till (0, 0) in a n * n square matrix, and print all the elements using recursion (similar to sudoku solver)
#Find all the digits sum within a given number using recursion.


