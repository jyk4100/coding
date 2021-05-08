# Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's 
## in their binary representation and return them as an array.
# Example 1:
# Input: 2
# Output: [0,1,1]
# Example 2:
# Input: 5
# Output: [0,1,1,2,1,2]


## division by 2 is right?/left? shift 
# 3 = 11 = 2+1
# 6 = 110 = 4+2 
# 12 = 1100 = 8+4
# 24 = 11000 = 16+8

num = 16
def countBits(num):
    bitcounts = [0,1,1,2,1,2,2,3]
    for i in range(8, num+1):
        ## division by 2 is "shifting" bits and +1 for odd numbers
        bitcounts.append( bitcounts[math.floor(i/2)] + (0 if i % 2 == 0 else 1) )
    return( bitcounts[:(num+1)] )

## end of function
countBits(16)

temp = bitcounts + bitcounts2
len(temp)



## gg
import math
bits = [0,1,1,2,1,2,2,3]
## 8 to 15
bits[8-4] + math.floor(8/4) - 2 # 8
bits[9-4] + math.floor(9/4) - 2 # 9
bits[12-8] + math.floor(12/4) - 2
bits[13-8] + math.floor(13/4) - 2
bits[14-8] + math.floor(14/4) - 2
bits[15-8] + math.floor(15/4) - 2
x = list(range(8, 16))
gg = [bits[n - 4*(math.floor(n/4)-1)] + math.floor(n/4) - 2 for n in x]
gg
bits = bits + gg
## but...
x = list(range(16, 24))
gg = [bits[n - 4*(math.floor(n/4)-1)] + math.floor(n/4) - 2 for n in x]
gg
bits[16 - 4*(math.floor(16/4)-1)] + math.floor(16/4) - 2
