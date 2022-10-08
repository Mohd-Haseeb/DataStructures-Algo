def floorSqrt(x): 
        if x==1:
            return 1
        
        low = 1
        high = x//2
        ans=0
        while low<=high:
            middle = low + (high-low)//2
            sqr = middle * middle
            
            if sqr==x:
                return middle
            
            if sqr > x:
                high = middle -1
            else:
                ans = middle
                low = middle + 1
        return ans

ans = floorSqrt(18)
print(ans)