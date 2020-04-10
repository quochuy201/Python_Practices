from collections import defaultdict
# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    cnt  ='Yes'
    dctmag = defaultdict(int)
    for word in magazine:
        dctmag[word] +=1
    for word in note:
        if dctmag[word] == 0 :
            cnt='No'
        dctmag[word] -=1
    print(cnt)
    
m = 'give me one grand today night'
n = 'give one grand today'
checkMagazine(m,n)
