n = int(input("n: "))

empty = '-'
queen = 'q'

b = [[empty]*n for i in range(n)]

def issafe(i,j):

    for p in range(n):
        if b[i][p] == queen or b[p][j] == queen:
            return False

    for x in range(n):
        for y in range(n):
            if i+j == x+y or i-j == x-y:
                if b[x][y] == queen:
                    return False

    return True


def nqueen(noq):
    if noq == 0:
        return True

    for i in range(n):
        for j in range(n):
            if b[i][j] != queen and issafe(i,j):
                b[i][j] = queen

                if nqueen(noq-1):
                    return True

                b[i][j] = empty

    return False


def printboard(b):
    for i in b:
        for j in i:
            print(j, end=" ")
        print()


# Place first queen
b[0][0] = queen

if nqueen(n-1):
    printboard(b)
else:
    print("Cant place")