# https://bit.ly/3P94D7O

# Find the minimum element in the sorted rotated array

def findMin(arr, n):
        l =0
        h=n-1
        
        while l<=h:
            mid = l+(h-l)//2
            
            if (mid==0) or arr[mid]<arr[mid-1]: # if mid < mid-1, then it means it is the smallest element in the array
                return arr[mid]
            if arr[mid+1]<arr[mid]: # if mid+1 < mid, then it means mid+1 is the smallest element in the array
                return arr[mid+1]
            
            # no rotation array , in this case minimum element is the first element
            if arr[l]<arr[mid] and arr[mid]<arr[h]:
                return arr[l]
            
            # left side sorted -> then min element is in unsorted region
            if arr[l]<arr[mid]:
                l = mid+1
            #right side sorted -> then min element is in unsorted region
            elif arr[mid]<arr[h]:
                
                h = mid-1
            else:
                return arr[l]
        return -1