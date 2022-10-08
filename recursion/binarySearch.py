
# BINARY SEARCH USING RECURSION
def binarySr(arr, num, left, right):

    # base condition
    if left>right: # O(1)
        return -1
    
    if left <= right:
        
        mid = left+(right-left)//2 # O(1)

        if arr[mid] == num: # O(1)
            return mid
        
        if arr[mid] > num:
            return binarySr(arr,num, left, right=mid-1) # O(n/2)
        else:                                               # OR
            return binarySr(arr,num, left=mid+1, right=right) # O(1)
    
# recurrence relation T(n) -> T(n/2) + C

# by using masters theorem ; a=1, b=2, k=0, p=0 => CASE 2 => O(log n)

# DRIVER CODE

if __name__=='__main__':

    arr = [2,4,6,8,12,15,20,24,30,33,40,42,80]
    ans = binarySr(arr,80,0,len(arr)-1)
    print(ans)