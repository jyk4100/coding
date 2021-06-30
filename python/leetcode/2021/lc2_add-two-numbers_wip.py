## leetcode 2 add linked list
## https://leetcode.com/problems/add-two-numbers/
## jyk4100 last modified: 2021-06-14

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
## gg linkedlist




## linkedlist 적응하는중? --------------------------------------------------------------------------------------------
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
## end of constructor
## function to print linkedlist?
def print_ll(x):
    while x != None: #true
        print(x.val)
        x = x.next
## create linkedlist from regular list
def l_to_ll(x):
    ll = ListNode(x[0])
    x = x[1:]
    tail = ll
    while(len(x)>0):
        tail.next = ListNode(x[0])
        tail = tail.next
        x = x[1:]
    return(ll)
## indent... 
x = l_to_ll([1,2,3])
print_ll(x)
## 적응은 개뿔....


## leetcode 26 remove duplicate in place -----------------------------------------------------------------------------------
mylist = [1,2,3,3,4]
## gg ppagasari... ㅠㅠ
for i in range(0,4,1): ## 0;<4;1++
    if mylist[i] == mylist[i+1]:
        mylist.remove(mylist[i])
        

## 04/25 linkedlist recap -----------------------------------------------------------------------------------
## class/constructor
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
## print 
def printll(x):
    while x != None: #while true
        print(x.val)
        x = x.next
## indent...
## create linkedlist from list
def ltoll(x):
    ll = ListNode(x[0])
    x = x[1:]
    tail = ll
    while len(x) > 0:
        tail.next = ListNode(x[0])
        x = x[1:]
        tail = tail.next
    return(ll)        
## indent...
temp = ltoll([1,2,3,4])  
printll(temp) 

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        