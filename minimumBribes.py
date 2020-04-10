q= [2,1,5,3,4]


Q = [p-1 for p in q]
move = 0
for i, p in enumerate(Q):
    if (p-i)>2:
        print('Too chaotic')
        break
        # From here on out, we don't care if P has moved
        # forwards, it is better to count how many times
        # P has RECEIVED a bribe, by looking at who is
        # ahead of P.  P's original position is the value
        # of P.
        # Anyone who bribed P cannot get to higher than
        # one position in front if P's original position,
        # so we need to look from one position in front
        # of P's original position to one in front of P's
        # current position, and see how many of those 
        # positions in Q contain a number large than P.
        # In other words we will look from P-1 to i-1,
        # which in Python is range(P-1,i-1+1), or simply
        # range(P-1,i).  To make sure we don't try an
        # index less than zero, replace P-1 with
        # max(P-1,0)
    for j in range(max(p-1,0),i):
        if(Q[j]>p):
            move +=1
print(move)
