

def helper(arr:list,minimum:int,maximum:int):
    if arr == []:
        return (minimum,maximum)
    
    if arr[0]>maximum:
        maximum = arr[0]
    
    if arr[0] < minimum:
        minimum = arr[0]
    
    helper(arr[1:],minimum,maximum)

arr = [23,45,23,7,4,89]
ans = helper(arr,arr[0],arr[0])
print(ans)
