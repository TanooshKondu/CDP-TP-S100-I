#LEETCODE 70, 746
def findPathCount(i, n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return findPathCount(n-1) + findPathCount(n-2)
    
n = int(input())
print(findPathCount(n))