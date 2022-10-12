# Given a positive integer num, write a program that returns True if num is a perfect square else return False. Do not use built-in functions like sqrt. Also, talk about the time complexity of your code.
# Test Cases:
# Input: 16
# Output: True

# Input: 14
# Output: False

def isPerfectSquare(num):
    start = 1
    end = num-1

    while start <= end:
        mid = start + (end-start)//2

        squared = mid*mid

        if squared == num:
            return True

        if squared > num:
            end = mid -1 
        else:
            start = mid + 1

    return False


# DRIVER CODE

if __name__ == "__main__":


    number = 19

    isPerfect = isPerfectSquare(number)

    if isPerfect:
        print(f"{number} is Perfect Square")
    else:
        print(f"{number} is NOT a Perfect Square")
        
