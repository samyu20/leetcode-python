#You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0
#Input: prices = [7,1,5,3,6,4] , Output: 5

def buy_and_sell(prices):                     #must buy before sell
    buy_price = prices[0]                     #b_p =7,1,1,1,1,1
    profit = 0                                #pro = 0 ,0, 4, 4, 5,5

    for p in prices [1:]:                     #7,   1,    5,     3,    6,   4
        if buy_price > p:                     # 7>1  , 1>5,  1>3  , 1>6  , 1>4
            buy_price = p                     #b_p= 1 , F , F  ,F , F

        profit = max(profit ,p - buy_price )  #max(0,1-1)=0, (0,5-1)=4, (4,3-1)=2 ,(4,6-1)=5 , (5,5-1)=4
    return  profit

prices = [7, 1, 5, 3, 6, 4]
print(buy_and_sell(prices))