m = [
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [1, 1, 0, 1, 0, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 1, 0, 0, 1],
    [0, 0, 1, 0, 0, 1],
]

def checkNeighbor(matrix, x, y, i, j):
    x += i
    y += j
    if (x == 0 or x == len(matrix) - 1 or y == 0 or y == len(matrix[0]) - 1) and matrix[x][y] == 1:
        return True
    elif matrix[x][y] == 0:
        return False
    if i != 1 and checkNeighbor(matrix, x, y, -1, 0):
            return True
    if i != -1 and checkNeighbor(matrix, x, y, +1, 0):
        return True
    if j != 1 and checkNeighbor(matrix, x, y, 0, -1):
        return True
    if j != -1 and checkNeighbor(matrix, x, y, 0, +1):
        return True
    return False

def removeIslands(matrix):
    i = len(matrix)
    j = len(matrix[0])
    # print (i, j)
    for x in range(1, i - 1):
        for y in range(1, j - 1):
            if matrix[x][y] == 1 and not checkNeighbor(matrix, x, y, 0, 0):
                matrix[x][y] = 5
            # print (x, y)
    return matrix

for i in m:
    print (i)
print ('---------------')
for i in removeIslands(m):
    print (i)
# print ()