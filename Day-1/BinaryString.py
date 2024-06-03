def prob(size, result, n):
    if size == n:
        print(result)
        return
    prob(size + 1, result + "1", n)
    prob(size + 1, result + "0", n)

n = int(input())
prob(0, " ",n)
    
#PRACTICE PROBLEMS
#https://pastebin.com/2yYrb7yN

#1. WRITE A PYTHON PROGRAM, TO ACCEPT A LIST OF INTEGERS AND PRINT THE SUM OF ALL 5 DIVISIBLE NUMBERS USING RECURSION

#2. write a python program to print all even indexed elements in both left to right and right to left manner using recursion.