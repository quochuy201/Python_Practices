def repeatedString(s, n):
    lst = list(s)
    cnt = lst.count('a')
    if cnt ==0:
        return 0
    elif cnt ==1 and len(s)==1:
        return n
    else:
        repreat = n//len(s)
        counta = repreat * cnt
        l = n % len(s)
        for i in range(l):
            if s[i] == 'a':
                counta +=1
        return counta

s ='jdiacikk'
n = 899491

print(repeatedString(s,n))


print(899491//8)
print(899491%8)
