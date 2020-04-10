def jumpingOnClouds(c):
    nstep =0
    i =0
    while i< len(c)-1:
        if (i == len(c)-2) or (c[i+2] ==1):
            i +=1
            nstep +=1
        else:
            i +=2
            nstep +=1
    return(nstep)

arr = input()
#0 0 1 0 0 1 0
c = list(map(int, arr.split()))
result = jumpingOnClouds(c)
print(result)
