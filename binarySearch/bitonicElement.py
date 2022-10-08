# https://bit.ly/3OOD2ck

# Find the bitonic element in the given bitonic array



def findMaximum(self,arr, n):
    l = 0
    h = n-1
    
    while(l<=h):
        mid = l + (h-l)//2
        
        # Check if mid element is bitonic element 
        if ((mid==0 or arr[mid]>arr[mid-1]) and (mid==n-1 or  arr[mid]>arr[mid+1])):
            return arr[mid]
        
        # if mid>mid+1, then it means array is increasing, so we have to move right side
        if (arr[mid]>arr[mid-1]):
            l = mid+1
        else:
            h = mid-1
        
        
    return -1