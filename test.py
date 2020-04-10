
arr = [1, 5, 4, 3, 2] 
arrpos = [*enumerate(arr)]

print(arr)
print(arrpos)
arrpos.sort(key = lambda it:it[1])
print(arrpos)
l=6
visited = [False]*l
print(visited)
