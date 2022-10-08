# Given a sorted 2D matrix, return whether the element is present or not in the matrix


# TIME COMPLEXITY =>  log(m * n) [optimmised approach]
def search2Darray(arr, target):
    # no of rows
    n = len(arr)
    if n==0:
        return False
     # no of colums
    m = len(arr[0])

    start = 0
    end = (m*n) -1

    while start <= end:
        mid = start + (end - start)//2

        mid_element = arr[mid//m][mid%m]

        if mid_element == target:
            return True
        
        if mid_element > target:
            end = mid -1
        else :
            start = mid + 1
    
    return False



if __name__ == '__main__':
    # DRIVER CODE
    arr = [[1,4,5,7], [9,12,16,18], [35,37,38,40], [55,57,58,90]]

    ans = search2Darray(arr,6)

    print(ans)