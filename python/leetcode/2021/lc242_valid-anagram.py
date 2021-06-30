## leetcode 242 valid-anagram
## jyk4100
## last modified: 2021-05-21

def isAnagram(s:str, t:str):
    s_dict = [0] * 26
    t_dict = [0] * 26
    for i in range(0, len(s)):
        # print(s_dict[i])
        s_dict[ord(s[i])-97] = s_dict[ord(s[i])-97] + 1
    for i in range(0, len(t)):
        # print(s_dict[i])
        t_dict[ord(t[i])-97] = t_dict[ord(t[i])-97] + 1
    return(s_dict == t_dict)

## too ez
# from collections import Counter
# hash_table = dict(Counter(s))
# hash_table2 = dict(Counter(t))
# hash_table == hash_table2

isAnagram("anagram", "nagaram")
