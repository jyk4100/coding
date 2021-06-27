## leetcode 3 longest substring without repeating characters
## https://leetcode.com/problems/longest-substring-without-repeating-characters/
## jyk4100
## last modified: 2021-06-20

## want to "slide window" and jump characters we already know are unique
## e.g. s = "abcabcbb"
## i=0 ~ i=2 add a, b, c, respectively
## cmap = {a:0, b:1, c:2} sub_start=0, max=3
## i=3, a is duplicated and "previously" a was at index 0 which is after our substr begin
## substring from 0+1 to i
## i=5
## cmap = {a:3, b:4, c:5} sub_start=3, max=3
## i=6, cmap[b] = 4 >= sub_start -> sub_start = 5

def longest_unique_sub(s):
    cmap = dict()
    sub_start = 0
    max_len = 0
    # sub_end = 0   
    for i in range(0,len(s)):
        if s[i] in cmap and cmap[s[i]] >= sub_start:
            sub_start = cmap[s[i]] + 1
            cmap[s[i]] = i   
            print("sub:{}".format(s[sub_start:(i+1)]))        
            max_len = max(max_len, i+1-sub_start)
            print(max_len)
        else: # s[i] not in cmap
            cmap[s[i]] = i
            print("sub:{}".format(s[sub_start:(i+1)]))
            max_len = max(max_len, i+1-sub_start)
            print(max_len)
    return(max_len)

longest_unique_sub('abcabcbb')
longest_unique_sub('pwwkew')
longest_unique_sub('dvdf')
longest_unique_sub('abba')

## prac and struggles --------------------------------------------------------
## when to jump?
def prac1(s):
    if len(s) == 0:
        return(0)
    s2 = s
    mymax = 1
    idx = 0
    charset = set(s[0])
    for i in range(1, len(s)):
        nxt_char = s2[i]
        print( "itr:{}, next char:{}, charset:{}".format(i, nxt_char, charset))
        if nxt_char in charset:
            s = s[1:]
            charset = set()
            charset.update(s[0:1])
            charset = s[0:1]
            mymax = max(len(charset), mymax)
            print("case 1 sub:{}, s:{}".format(charset, s))
        else: 
            charset.add(nxt_char)
            mymax = max(len(charset), mymax)
            print("case 2 sub:{}, s:{}".format(charset, s))
    return(charset, mymax)

## ggwp2
def prac2(s):
    if len(s) == 0:
        return(0)
    s2 = s
    sub = s[0]
    mymax = 1
    for i in range(1, len(s)):
        nxt_char = s2[i]
        if nxt_char in sub:
            s = s[1:]
            sub = s[0]
            sub = sub + nxt_char
            mymax = max(len(sub), mymax)
            print( "1 sub:{}, nxt_char:{}, s:{}".format(sub, nxt_char, s))
        else: 
            sub = sub + nxt_char
            mymax = max(len(sub), mymax)
            print( "2 sub:{}, net_char:{}, s:{}".format(sub, nxt_char, s))
    return(sub, mymax)

## when to "skip" ???
prac2("pwwkew")
prac2("aabaab!bb")
prac2("dvdf")