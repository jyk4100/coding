## leetcode 14 longest-common-prefix
## https://leetcode.com/problems/longest-common-prefix/
## jyk4100
## last modified: 2021-06-30

strs = ["flower","flow","flight"]
strs = ["dog","racecar","car"]
strs = ['flower','flower','flower']
strs = ['']
strs = ['a']
strs = ['','']
strs = ["abab","aba",""]

## basically brute-force compare one string by one but tried to exist/break asap
def longestCommonPrefix(strs):
    ## omg edge cases
    strs.sort()
    if len(strs) <= 1 or any([x == '' for x in strs]):
        return strs[0]
    else:
        k = 0
        check = 0
        for j in range(0,len(min(strs))):
            for i in range(1,len(strs)):
                if (strs[0][k] != strs[i][k]):
                    break
                else:
                    check = check + 1
                    print(strs)
            if check == (len(strs)-1):
                check = 0
                k = k + 1
            else:
                break
        return strs[0][0:k]

longestCommonPrefix(strs)

## "do-while" doesn't work with edge cases like
# def longestCommonPrefix(self, strs: List[str]) -> str:
#     if len(strs) <= 1 or any([x == '' for x in strs]):
#         return strs[0]
#     else:
#         char = strs[0][0]
#         strs[0] = strs[0][1:]
#         check = 0
#         ss = ""
#         for j in range(0,len(min(strs))):
#             for i in range(1,len(strs)):
#                 if (char != strs[i][0]):
#                     break
#                 else:
#                     strs[i] = strs[i][1:]
#                     check = check + 1
#                     # print(strs)
#             if check == (len(strs)-1):
#                 check = 0
#                 ss = ss + char
#                 char = strs[0][0]
#                 strs[0] = strs[0][1:]
#             else:
#                 break
#     return(ss)