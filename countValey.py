def countingValleys(n, s):
    strs= s.split()
    ints = [1 if i =='U' else -1 for i in s]
    countvl =0
    path = 0
    isdown = False
    for s in ints:
        path += s
        if (path <0 )and not isdown:
            isdown = True
        if (path ==0 ) and isdown:
            countvl +=1
            isdown = False
    return countvl
arr = input()
n = len(arr)
result = countingValleys(n, arr)
print(result)
