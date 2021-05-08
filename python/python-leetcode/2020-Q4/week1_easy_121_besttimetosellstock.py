## 2020-10-15 leetcode practice
## 확실히 스터디를 등록해노니까 할수밖에 없네 ㅋㅋㅋ 상황이 사람을 만든다 ㅇㅇ
## wifi 안되니까 복붙 대신 대충
# input: [7,1,5,3,6,4]
# output: 5
# explanation: buy on day 2 (price=1) and sell on on day 5 (price=6)
# input: [7,6,4,3,1]
# output: 0
# explanation: no transaction is best

## double loop bruteforce ggwp time line exceed
def maxProfit(prices):
    maxprofit = 0
    maxi = 0
    maxj = 0
    for i in range(len(prices)-1, -1, -1):
        for j in range(i-1, -1, -1):
            # print("i:{}, j:{}, profit{}".format(i,j,plist[i]-plist[j]))
            if (prices[i] - prices[j] > maxprofit):
                maxprofit = prices[i] - prices[j]
                maxi = i
                maxj = j
    # print("i:{}, j:{}".format(maxi,maxj))
    return(maxprofit)
## testcases
prices = [7,1,5,3,6,4]
prices = [7,6,4,3,1]
prices = [2,4,1]
maxProfit(prices)

prices = [2,4,1]

# ## 그냥 의식의 흐름대로 해보면.... 안됨 뒤에서 min 이 나오는 경우 ㅈㅈ
# def computeprofit_gg(plist):
#     buyp = plist[0]
#     sellp = plist[0]
#     buyi = 0
#     selli = 0
#     for i in range(0, len(plist)-1):
#         if plist[i+1] < plist[i] and plist[i+1] < buyp:
#             buyp = plist[i+1]
#             buyi = i + 1
#             sellp = buyp
#         ## sellp must "follow" 
#         elif plist[i+1] > plist[i] and plist[i+1] > sellp:
#             sellp = plist[i+1]
#             selli = i + 1
#         ## indent...
#     print("buy on day {} for {} and sell on day {} for {}".format(buyi, buyp, selli, sellp))
#     if selli == 0: 
#         print("no transaction made")
#     else:
#         return(sellp - buyp)


## find max profit
def maxProfit(prices):
    ## edge case when prices list empty
    minprice = prices[0] if len(prices) > 0 else 0
    maxprofit = 0
    ## iterate over list
    for i in range(0, len(prices)):
        minprice = min(minprice, prices[i])
        ## only if "nextday" price is greater and maxprofit is higher update maxprofit
        if prices[i] > minprice and prices[i] - minprice > maxprofit:
           maxprofit = prices[i] - minprice 
    print("minprice:{}".format(minprice))
    return(maxprofit)
maxProfit(prices=[7,1,5,3,6,4])
maxProfit(prices=[2,4,1])
maxProfit(prices=[])











