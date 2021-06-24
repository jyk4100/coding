## leetcode 7 reverse-integer
## https://leetcode.com/problems/reverse-integer/
## jyk4100
## last modified: 2021-06-23

def reverse_int(x):
    rev = (1 if x >=0 else -1) * int(str(abs(x))[::-1])
    if -2**31 <= rev and rev <= 2**31 - 1:
        return(rev) 
    else:
        return(0)

# Input: x = 123
# Output: 321
# Input: x = -123
# Output: -321
# Input: x = 120
# Output: 21
# Input: x = 0
# Output: 0

def reverse_int(x):
    rev = 0
    abx = abs(x)
    while abx > 0:
        q = abx % 10
        rev = q + rev * 10
        abx = int(abx/10)
    rev = (1 if x >=0 else -1) * rev
    if (-2**31 <= rev and rev <= 2**31 - 1):
        return(rev)
    else:
        return(0)

reverse_int(321)
reverse_int(-123)
