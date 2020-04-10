from collections import Counter
from itertools import combinations
def sherlockAndAnagrams(s):
    substring = [''.join(sorted(s[i:j])) for i in range(len(s)) for j in range(i + 1, len(s)+1)]
    b= Counter(substring)
    result =0
    for key, value in b.items():
        result +=(value*(value-1)/2)
    return(int(result))


s = 'abba'

print(sherlockAndAnagrams(s))
