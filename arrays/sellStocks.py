# Find the best time to buy and sell the stocks


# Time Complexity => O(n^2) 
def buySell(arr):
    diff = []
    pairs = []

    # looping through all the elements of array one by one
    for i in range(len(arr)):
        buy = arr[i]
        temp_diff = -1
        sell = -1
        for j in range(i+1, len(arr)):
            if arr[j] > buy:
                t = arr[j] - buy
                if t > temp_diff:
                    temp_diff = t
                    sell = arr[j]
        diff.append(temp_diff)
        pairs.append((buy,sell))
    return diff,pairs


# TIME COMPLEXITY => O(N)
def buySellOptimized(arr):
    minPrice = float('inf')
    maxProfit = 0

    for i in range(len(arr)):
        if arr[i] < minPrice:
            minPrice = arr[i]
        elif arr[i] - minPrice > maxProfit:
            maxProfit = arr[i] - minPrice
    
    return maxProfit




if __name__ == "__main__":

    # DRIVER CODE

    prices = [7,4,5,3,6,16]

    ans, days = buySell(prices)

    profit = buySellOptimized(prices)

    print(ans)
    print(days)

    print(f"optimized profit => {profit}")

