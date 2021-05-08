## leetcode easy 190
# The input must be a binary string of length 32
# Input: n = 00000010100101000001111010011100
# Output: 964176192 (00111001011110000010100101000000)
# Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, 
# so return 964176192 which its binary representation is 00111001011110000010100101000000.

## leetcode solution class input format?
def reverseBits(n, digits=32):
    n = str(n)
    rev_binary_powers = [2**x for x in range(0,digits)]
    reverse_decimal = sum( [int(x) * y for x,y in zip(n, rev_binary_powers)] )
    # print("decimal representation of reversed binary representation of {}: {}".format(n, reverse_decimal))
    return(reverse_decimal)
reverseBits('00000010100101000001111010011100') ## 964176192
reverseBits('11111111111111111111111111111101') ## 3221225471
# x = 00000010100101000001111010011100


reverseBits('01011000',8)
reverseBits('1011000',7)
reverseBits('1010',4)

## solution...
def reverseBits(self, n):
    ret, power = 0, 31
    while n:
        ret += (n & 1) << power
        n = n >> 1
        power -= 1
    return ret
11 >> 3 ## bit shift operator???
    




# [2**x for x in range(31,-1,-1)]
# sum( [int(x) * y for x,y in zip(bits, binary_powers)] )

## tidy function
def bits_to_decimal(bits, powers):    
    decimal_list = [int(x) * y for x,y in zip(bits, powers)]
    return( sum(decimal_list) )
## end of function
bits_to_decimal('00000010100101000001111010011100', [2**x for x in range(31,-1,-1)])

decimal = 39
remainder = decimal
binary_list = list()
for i in range(0,32):
    if remainder % binary_powers[32-1-i] < remainder:
        remainder = remainder - binary_powers[32-1-i]
        binary_list.append('1')
    else:
        binary_list.append('0')
''.join(binary_list)


## with reversed "powers" in mind...
def decimal_to_binary(decimal, binary_powers):
    remainder = decimal
    binary_list = list()
    for i in range(0,32):
        if remainder % binary_powers[32-1-i] < remainder:
            remainder = remainder - binary_powers[32-1-i]
            binary_list.append('1')
        else:
            binary_list.append('0')
    return(''.join(binary_list))
## end of function

decimal_to_binary(43261596, [2**x for x in range(0,len(bits))])
decimal_to_binary(43261596, [2**x for x in range(0,len(bits))])


