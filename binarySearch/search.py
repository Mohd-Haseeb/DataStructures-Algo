# https://bit.ly/3bQwlb0



def Search(arr,n,k):
    l = 0
    h = n-1
    
    while l<=h:
        mid = l + (h-l)//2
        
        if arr[mid]==k:
            return mid
        
        # left side is sorted
        if arr[l]<arr[mid]:
            if arr[l]<=k and k<arr[mid]: # element present in the sorted section
                h = mid-1
            else:
                l = mid+1
        else: # right side is sorted
            if arr[mid]<k and k <= arr[h]:
                l = mid+1
            else:
                h = mid-1
    return -1

arr = [5,6,7,8,9,10,1,2,3]
n = len(arr)
k=10
index_of_k = Search(arr,n,k)

print(index_of_k)


