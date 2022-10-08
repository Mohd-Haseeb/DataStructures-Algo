# We have an array, unsorted. After a certain point the numbers are only Infinites.
# Size of array is N.
# Return the index of first occurence of 'infinite'



def binaryS(arr:list, n:int) -> int:
    start = 0
    end = n-1

    while (start <= end):
        mid = start + (end-start)//2

        if arr[mid] == 'i' and arr[mid-1] != 'i':
            return mid
        elif arr[mid]=='i' and arr[mid-1] == 'i':
            end = mid-1
        else:
            start = mid +1


# Another approach is linear search (NOT OPTIMISED)

# Q2. What if value of N is not given?
def binaruSModified(arr:list):
    start = 0
    end = 1

    while start<=end:
        mid = start + (end-start)//2

        if arr[mid]=='i':
            return (start,end)
        else:
            start = end +1
            if end==1:
                end = 3
            else:
                end = end**2




## DRIVER CODE
arr = [2,10,12,65,12,-23,43,'i','i','i','i']


ans = binaruSModified(arr)

print(ans)

# print(binaryS(arr, len(arr)))
        
            




