


def flood(i,j,image,n,m,oldColor,newColor):
    if (i < 0 or j < 0 or i==n or j ==m or image[i][j] != oldColor):
        return
    image[i][j] = newColor
    flood(i+1,j,image,n,m,oldColor,newColor)
    flood(i-1,j,image,n,m,oldColor,newColor)
    flood(i,j+1,image,n,m,oldColor,newColor)
    flood(i,j-1,image,n,m,oldColor,newColor)
    


def floodFill(image, x, y, newColor):
    oldColor = image[x][y]
    if oldColor == newColor:
        return image
   
    n = len(image)

    m = len(image[0])
    flood(x,y,image,n,m,oldColor,newColor)
    return image

img = [[1,2,1,2,3,5],[1,2,2,4,3,4],[1,2,4,4,5,4],[6,2,2,2,3,4],[7,6,1,3,3,3]]
newAns = floodFill(img,1,3,9)
print(newAns)