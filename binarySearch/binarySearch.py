# Liner search => O(n)

def binarySearch(number,arr):
    start = 0
    end = len(arr)-1

    while start<=end:
        middle = (start+end)//2

        if arr[middle]==number:
            return f"{number} is present at index {middle}"
        
        if arr[middle]>number:
            end = middle-1
        else:
            start = middle+1
        
    return "Not Present"



# DRIVER CODE
if __name__ == "__main__":


    arr = [2,4,6,8,12,15,20,24,30,33,40,42,80]
    ans = binarySearch(2,arr)
    print(ans)