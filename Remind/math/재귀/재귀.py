def fibo(x):
    # base case
    if x == 0:
        return 0
    if x == 1:
        return 1
    
    # recursive case
    return fibo(x - 1) + fibo(x - 2)


n = int(input())
print(fibo(n))

# 2^N 