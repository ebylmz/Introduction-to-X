def main():
    triangleRight(5)

def square(row, col):
    for i in range(row):
        for j in range(col):
            print("#", end="")
        print()

def triangleRightHelper(height, space):
    if height == 0:
        return
    else:
        triangleRightHelper(height - 1, space + 1)

        for i in range(space): print(" ", end="")
        for i in range(height): print("#", end="")
        print()

def triangleRight(height):
    triangleRightHelper(height, 0)

def triangleLeft(height):
    if height <= 0:
        return
    else:
        # draw the height - 1 triangle
        triangleLeft(height - 1)
        # add last row to complete triangle
        for i in range(height):
            print("#", end="")
        print() # default value of end is "\n"


main()