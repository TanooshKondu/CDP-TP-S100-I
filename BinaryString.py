def prob(size, result, n):
    if size == n:
        print(result)
        return
    prob(size + 1, result + "1", n)
    prob(size + 1, result + "0", n)

n = int(input())
prob(0, " ",n)
    
#PRACTICE PROBLEMS

#1. WRITE A PYTHON PROGRAM, TO ACCEPT A LIST OF INTEGERS AND PRINT THE SUM OF ALL 5 DIVISIBLE NUMBERS USING RECURSION

#2.WRITE A PYTHON PROGRAM, TO PRINT ALL EVEN INDEXED