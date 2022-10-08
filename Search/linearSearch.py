
# Time Complexity = O(n)
# Space Complexity = O(1)

# LINEAR SEARCH
def linearSearch(arr:list, num:int) -> int:
    for i in range(len(arr)):
        if arr[i] == num:
            return i
    return -1







if __name__ == "__main__":
    


    # DRIVER CODE
    myArr = [12,15,87,44,98,34,3]
    find = 87

    # FUNCTION CALLING
    index_find = linearSearch(myArr, find)

    print(f"{find} is present at index {index_find}")

