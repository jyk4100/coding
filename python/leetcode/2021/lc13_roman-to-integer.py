## leetcode 13 Roman to Integer
## https://leetcode.com/problems/roman-to-integer/
## jyk4100
## last modified: 2021-06-30

cmap = dict({'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000})

def romantoint(s):
    i = [cmap[x] for x in s]
    ilag = [x - y for x,y in zip(i[0:(len(s)-1)], i[1:len(s)])] + [0]
    sign = [-1 if x < 0 else 1 for x in ilag]
    temp = [x * y for x,y in zip(i, sign)]
    return(sum(temp))

romantoint('IV')
romantoint('VI')
romantoint('LVIII')
romantoint('MCMXCIV')
