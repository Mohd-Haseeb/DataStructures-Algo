def fastPower(a,b):
    if b==0:
        return 1
    
    halfRes = fastPower(a, b//2)

    fullRes = halfRes * halfRes

    if b%2 != 0:
        fullRes *= a
    
    return fullRes


ans = fastPower(8,12)
print(ans)

