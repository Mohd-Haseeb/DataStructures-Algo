# https://practice.geeksforgeeks.org/problems/spirally-traversing-a-matrix-1587115621/1/

def spirallyTraverse(self,matrix, r, c): 
        left = 0
        right = c-1
        top = 0
        bottom = r-1
        arr=[]
        
        while(left<=right and top <= bottom):
            for i in range(left,right+1):
                arr.append(matrix[top][i])
            top += 1
            
            for i in range(top,bottom+1):
                arr.append(matrix[i][right])
            right -= 1
            
            if top<=bottom:
                for i in range(right,left-1,-1):
                    arr.append(matrix[bottom][i])
                bottom -=1 
            
            if left <= right:
                for i in range(bottom,top-1,-1):
                    arr.append(matrix[i][left])
                left += 1
        return arr