def maximumRods(n, a, b, c):
    if n==0:
        return 0
    if n<0:
        return -1
    
    cutA = maximumRods(n-a, a, b, c) + 1
    cutB = maximumRods(n-b, a, b, c) + 1
    cutC = maximumRods(n-c, a, b, c) + 1

    res = max(cutA, max(cutB, cutC))
    if res==-1:
        return -1
    return res

n = 17
ans = maximumRods(17, 10, 11, 3)
print("Answer : ",ans)
    