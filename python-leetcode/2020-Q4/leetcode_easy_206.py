## leetcode study prep & linkedlist recap
## linkedlist 적응하는중?
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
## end of constructor
## function to print linkedlist
def print_ll(x):
    while x != None:
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
llist = l_to_ll([1,2,3])
print_ll(llist) ## 적응은 개뿔 ㅋㅋㅋ


## 2020-10-22 reverse linkedlist 
## iterative solution
## 아 포인터 3개로 굳이 새로 만들고 할필요없이 가능?
llist = l_to_ll([1,2,3,4,5])
print_ll(llist)

## 아 자꾸 circular ref 되는게 처음에 NULL 지정.... ㅇㅇ....
## some while loop
p1 = None
p2 = llist

p3 = p2.next

p2.next = p1
p2 = p3
p1 = p2
p3 = p3.next

print_ll(p1)
print_ll(p2)
print_ll(p3)


## some while loop
p1 = None
p2 = llist

p3 = p2.next
p2.next = p1
p1 = p2
p2 = p3

print_ll(p1)
print_ll(p2)
print_ll(p3)
print_ll(llist)



## loop over
y = ListNode(tail.next.val)
y.next = ListNode(tail.val)
head = y
tail = llist.next
y = ListNode(tail.next.val)
y.next = head
print_ll(head)
print_ll(y)
print_ll(tail)