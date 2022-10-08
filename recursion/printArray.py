def forwardPrint(arr:list,n:int,present:int):
    if present == n:
        return
    
    print(arr[present], end=' ')
    forwardPrint(arr,n,present+1)


def reversePrint(arr:list,n:int,present:int):
    if present == n:
        return
    
    reversePrint(arr,n,present+1)
    print(arr[present], end=' ')


arr = [23,45,23,7,4,89]
n = len(arr)
# forwardPrint(arr,n,0)
reversePrint(arr,n,0)