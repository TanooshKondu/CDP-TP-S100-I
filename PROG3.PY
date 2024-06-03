def prog(i, n):
    if i>n:
        print("Base condition g0t hit")
        return
    print("Ending line:",i)
    for j in range(1,i):
        print(j)
    prog(i + 1, n)
    print("Starting line", i)
prog(1,8)