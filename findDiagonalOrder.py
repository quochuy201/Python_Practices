mat = [[1, 2, 3], 
        [4, 5, 6], 
        [7, 8, 9] ]
r = len(mat)
c = len(mat[0])

i,j=0,0
k=0
print(type(mat))
print(r, c)
isup = True
while k<c * r:
    if isup:
        while i >=0 and j < c:
            lst.append(matrix[i][j])
            k +=1
            j +=1
            i -=1
        if i< 0 and j < c :
            i = 0
        if j == c:
            i +=2
            j -=1
    else:
        while j >=0 and i < r:
            lst.append(matrix[i][j])
            k+=1
            i +=1
            j -=1
        if j< 0 and i < r :
            j = 0
        if i == r:
            j +=2
            i -=1

    isup = not isup
