

memo = {}

def fibo(n):
    if n in memo:
        return memo[n]
    
    if n <= 2:
        return 1
    
    result = fibo(n-1) + fibo(n-2)
    
    memo[n] = result

    return result



print(fibo(100))