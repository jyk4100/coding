## container with most water
## 각각의 vertical line의 길이고 제일 큰 사각형을 만들어야됨 ㅇㅇ
## (i, ai) coordinate ㅇㅇ
## test case1
# input: height = [1,8,6,2,5,4,8,3,7]
# output: max Area: 49
# 왜냐면 max height 이 8, 7 해서 7 which give width of 7
## [4,3,2,1,4] -> 16
## [1,2,1] -> 2
## [1,1] -> 1
## hint2: start with wider container and go narrower?

import math
left = 1
right = len(height) - 1

## 일단 계속 쓸건 function 으로 만들어놓고
def computeArea(height, left, right): 
    print("left:{}, right:{}, left_height:{}, right_height:{}".format(left, right, height[left], height[right]))
    return( min(height[left], height[right]) * (right - left) ) 
## indent...

left = 1
right = len(height) - 1
test2 = [1,3,9,4,20,7,2,12,6]
computeArea(test2, 2, 6)
## 3 에서 9로 인덱스 +2 인데 value 차이는 6 value 차이가 더 큼 ㅇㅇ
# cumdiff = [x - y for x,y in zip(test2[1:], test2[:len(test2)-1])]
# len(cumdiff)
# cumdiff[0:math.floor(len(cumdiff)/2)]

# height = [1,8,6,2,5,4,8,3,7]
height = [1,1]
height = [2,3,10,5,7,8,9] ## 36
height = [2,3,4,5,18,17,6] ## 아 중간에서 안됨 ㅈㅈ
height = [1,3,2,5,25,24,5]
def maxArea(height):
    left = 0
    right = len(height) - 1
    maxArea = min(height[left], height[right]) * (right - left)
    while left < right:
        if height[left] < height[right]:
        ## if height[left] < height[left+1]:
            left = left + 1
            print("left:{}, right:{}, left_height:{}, right_height:{}".format(left, right, height[left], height[right]))
        else:
            right = right - 1
            print("left:{}, right:{}, left_height:{}, right_height:{}".format(left, right, height[left], height[right]))
        maxArea = max(maxArea, min(height[left], height[right]) * (right - left) )
    return(maxArea)
maxArea(height)





## gg my solution 1 fail 
## tidy up
# height = [3,3,9,4,7,2,12,6]
height = [1,8,6,2,5,4,8,3,7]
left = 0
for i in range(0, math.floor(len(height)/2)):
## left
    if height[i+1] - height[i] > i - left and height[i+1] - height[left] > i - left:
        left = i + 1
## right
right = len(height)-1
for i in range(len(height)-1,math.floor(len(height)/2)-1, -1):
    if height[i-1] - height[i] > right - i and height[i-1] - height[right] > i - right:
        right = i - 1
computeArea(height, left, right)
height[left]
height[right]
## "높이" 가 늘어나는 만큼 "넓이"가 늘어나느냐 또 최대 높이 keep track? ## 너비 * 높이 바뀌는것도 감안해야됨... gg....

## gg my solution2 fail
import math
## function
def computeArea(height, left, right): 
    print("left:{}, right:{}, left_height:{}, right_height:{}".format(left, right, height[left], height[right]))
    return( min(height[left], height[right]) * (right - left) ) 
## function
def maxArea(height):
    left = 0
    right = len(height) - 1
    maxArea = computeArea(height, left, right)
    mid = math.floor(len(height)/2)
    if height[left] < max(height[left:mid]) and left < mid:
        left = left + 1
        maxArea = max(maxArea, computeArea(height, left, right))
    if height[right] < max(height[mid:right]) and mid > right:
        right = right - 1
        maxArea = max(maxArea, computeArea(height, left, right))
    return(maxArea)
##
# height = [1,8,6,2,5,4,8,3,7]
height = [1,1]
height = [2,3,10,5,7,8,9] ## 36
height = [2,3,4,5,18,17,6] ## 아 중간에서 안됨 ㅈㅈ
maxArea(height)
