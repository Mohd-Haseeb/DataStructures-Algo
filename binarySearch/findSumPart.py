# Q. Say a sorted array is given and  a taget value is given. we have to find a pair in the array suc that their sum is equal to target
# arr [10,20,40,58,70,80,110,140] , target = 120.

# Approach 1 => Linear Search (Brute force) -> O(n^2)
# Approach 2 => Binary Search -> O(n*log n)
# Approach 3 => Using 2 pointers (optimised) -> O(n)


# LINEAR SEARCH

def linearApproach(arr):
    pass


def bianryApproach():
    pass


# TWO POINTER APPROACH
# TIME COMPLEXITY = O(n)
def twoPointerApproach(arr, target):
    start = 0
    end = len(arr)-1

    while start <= end:
        if arr[start]+arr[end] == target:
            return (start, end)
        elif arr[start]+arr[end] < target:
            start += 1
        else:
            end -= 1
    return (-1,-1)




# DRIVER CODE

arr = [20,30,45,60,70,90,110,120,280]

a,b = twoPointerApproach(arr, target=150)

print(a,b)