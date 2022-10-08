# 0,1,1,2,3,5,8,......

def fib(n:int):
    if n==0 or n==1:
        return 1
    
    return fib(n-1) + fib(n-2)

print(fib(4))