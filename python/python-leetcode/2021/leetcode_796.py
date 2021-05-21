## leetcode 796 rotate-string 
## jyk4100
## last modified: 2021-05-21

def isRotated(s, goal):
    if len(s) != len(goal):
        return False
    if len(s) == 0:
        return True       
    sol=False
    for i in range(0,len(s)):
        # print(i)
        # print((s[i:] + s[:i]))
        if (s[i:] + s[:i]) == goal:
            sol=True
    return(sol)


isRotated(s='abcde', goal='cdeab')
