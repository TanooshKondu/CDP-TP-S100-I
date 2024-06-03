#Recursion Program print 10 nums using recursion


def prog(i,n):
    if (i >= n):
        return
    print(i)
    prog(i+1, n)
    
i = int(input())
n = int(input())
prog(i,n)