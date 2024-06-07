def FibanoccaiSeries(n):
    if n <= 1:
        return n
    else:
        FIB = FibanoccaiSeries(n-1) + FibanoccaiSeries(n-2)
    return FIB
n = int(input())
print(FibanoccaiSeries(n))

    