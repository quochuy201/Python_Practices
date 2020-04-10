from collections import Counter
from itertools import combinations
def countTriplets(arr, r):
    count = 0
    #arr = list(map(int,arr.split('')))
    if r == 1:
        count = (len(arr)-1)*(len(arr)-2)*len(arr)/6
    else:
        n = list(combinations(list(range(len(arr))),3))
        for i in n:
            if (arr[i[1]]/arr[i[0]] == r ) and (arr[i[2]]/arr[i[1]] ==r) :
                count +=1

    return(int(count))

##    
##def countTriplets(arr, r):
##
##    r2 = Counter()
##    r3 = Counter()
##    count = 0
##    
##    for v in arr:
##        if v in r3:
##            count += r3[v]
##        
##        if v in r2:
##            r3[v*r] += r2[v]
##        
##        r2[v*r] += 1
##
##    return count

arr =[1237]*100000
r =1
print(countTriplets(arr, r))
#n = list(combinations(list(range(arr)),3))
    
print((len(arr)-1)*(len(arr)-2)*len(arr)/6)
