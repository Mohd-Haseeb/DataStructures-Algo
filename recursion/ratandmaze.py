
def help(i,j,n,arr,path,ans):

    if (i<0 or j<0 or i==n or j==n or arr[i][j]==0):
        return
    
    elif i == n-1 and j == n-1:
        ans.append(path)
        return
    arr[i][j] = 0
    # up
    path += 'D'
    help(i+1,j,n,arr,path,ans)
    path = path[:-1]
    
    path += 'L'
    help(i,j-1,n,arr,path,ans)
    path = path[:-1]
    
    path += 'R'
    help(i,j+1,n,arr,path,ans)
    path = path[:-1]
    
    path += 'U'
    help(i-1,j,n,arr,path,ans)
    path = path[:-1]
        
    arr[i][j] = 1

def searchMaze(arr, n):
    # Write your code here.
    
    path =''
    ans = []
    help(0,0,n,arr,path,ans)
    print(ans)
arr = [[1,0,0,0],[1,1,0,0],[1,1,0,0],[0,1,1,1]]
n = len(arr)
searchMaze(arr,n)