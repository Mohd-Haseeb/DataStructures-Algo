def helper(res:list, N:int, present:int, inc:bool):
    res.append(present)

    if inc:
        if present==N:
            return
        else:
            helper(res,N,present+5,True)
    else:
        if present-5 > 0:
            helper(res,N,present-5,False)
        else:
            helper(res,N,present-5,True)


def helper2(res:list,present:int):
    if present<=0:
        res.append(present)
        return
    res.append(present)
    helper2(res,present-5)
    res.append(present)

def pattern(N):
    res = []

    # helper(res,N,N,False)
    helper2(res,N)

    return res

n = 16

ans = pattern(n)

print(ans)