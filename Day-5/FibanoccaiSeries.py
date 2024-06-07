def FibanoccaiSeries(n):
    if n <= 1:
        return n
    else:
        return FibanoccaiSeries(n-1) + FibanoccaiSeries(n-2)
n = int(input())
print(FibanoccaiSeries(n))

    