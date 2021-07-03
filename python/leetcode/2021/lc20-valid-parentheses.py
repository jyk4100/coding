## leetcode 20 validate parenthesis
## https://leetcode.com/problems/valid-parentheses/
## jyk4100
## last modified: 2021-07-03

cmap = {'{':'}', '(':')', '[':']'}
def validate_parenthesis(s):
    opn = []
    for char in s:
        if char in cmap.keys(): ## opening
            opn.append(char)
        else:
            if len(opn) > 0 and char == cmap[opn[-1]]:
                opn = opn[0:-1] ## "pop"
            else:
                return (False)
    return (len(opn) == 0)

validate_parenthesis("()")
validate_parenthesis("()[]{}")
validate_parenthesis("{[]}")
validate_parenthesis("(]")
validate_parenthesis("([)]")
validate_parenthesis(']')
validate_parenthesis("){")
validate_parenthesis("(([]){})")
validate_parenthesis("(){}}{")
validate_parenthesis("((")

## while loop version but really no diff
cmap = {'{':'}', '(':')', '[':']'}
def validate_parenthesis(s):
    opn = []
    valid = True and (len(s) % 2 == 0)
    while (len(s) > 0 and valid):
        if s[0] in cmap.keys():
            opn.append(s[0])
            s = s[1:]
        else:
            if len(opn) > 0 and s[0] == cmap[opn[-1]]:
                opn = opn[0:-1]
                s = s[1:]
            else:
                valid = False
    return(valid and len(opn) == 0)

# ## nope doesn't work with ([]){}
# cmap = {'{':'}', '(':')', '[':']', ')':'0', ']':'0', '}':'0'}
# def validate_parenthesis(s):
#     valid = True and (len(s) % 2 == 0)
#     while (len(s) > 0 and valid):
#         if cmap[s[0]] == s[len(s)-1]:
#             s = s[1:(len(s)-1)]
#         elif cmap[s[0]] == s[1]:
#             s = s[2:]
#         else:
#             valid = False
#         print(s)
#     return valid