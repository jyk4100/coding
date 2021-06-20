## leetcode 3 longest substring without repeating characters
## jyk4100 last modified: 2021-06-20

s = "abcabcbb"
s = "pwwkew"
s = "dvdf"
s = "abba"

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
longest_unique_sub('abba')
longest_unique_sub('dvdf')

# s = 'abcabcbb'
# l = 0
# mm = 0
# for i in range(len(s)):
#     while s[i] in charset:
#         print(i)
#         charset.remove(s[i])
#         l = l + 1
#         print(l, charset)
#     charset.add(s[i])
#     mm = max(mm, i - l + 1)

## prac and struggles --------------------------------------------------------
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
            # charset = set()
            # charset.update(s[0:1])
            charset = s[0:1]
            mymax = max(len(charset), mymax)
            print( "   1 sub:{}, s:{}".format(charset, s))
        else: 
            charset.add(nxt_char)
            mymax = max(len(charset), mymax)
            print( "   2 sub:{}, s:{}".format(charset, s))
    return(charset, mymax)

## fufu 
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