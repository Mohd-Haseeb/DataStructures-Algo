



def basic():
    for i in range(5):
        for j in range(5):
            print("* ", end='')
        print()

# basic()

def basicWithSpace():
    row = 5
    col = 5
    for i in range(row):
        for j in range(col):
            if (i==0) or (i==row-1) or (j==0) or (j==col-1):
                print("* ", end='')
            else:
                print("  ", end='')
        print()

# basicWithSpace()

def basicZ():
    row = 5
    col = 5
    for i in range(row):
        for j in range(col):
            if (i==0) or (i==row-1) or (j!=i) and (j>i):
                print("* ", end='')
            else:
                print("  ", end='')
        print()

# basicZ()

def upperTriangle():
    row = 5
    col = 5

    for i in range(row):
        for j in range(col):
            if(i<=j):
                print("* ", end='')
            else:
                print("  ", end='')
        print()

# upperTriangle()

def lowerTriangle():
    row = 5
    col = 5

    for i in range(row):
        for j in range(col):
            if(i>=j):
                print("* ", end='')
            else:
                print("  ", end='')
        print()

# lowerTriangle()


#      *
#     ***
#    *****
#     ***
#      *

def diamondPattern():
    height = 4
    for i in range(height):
        print(" "*(height-i-1),"* "*(i+1))
    for i in range(height):
        print(" "*(i+1),"* "*(height-i-1))
diamondPattern()
