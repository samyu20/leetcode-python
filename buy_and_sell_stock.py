"""Problem: #121. Best Time to Buy and Sell Stock
Given an array `prices` where prices[i] is the price of a stock on the i-th day,
maximize profit by choosing ONE day to buy and a LATER day to sell.

Return the maximum profit achievable.
If no profit is possible, return 0.

Example:
Input : prices = [7, 1, 5, 3, 6, 4], Output: 5"""

# Algorithm:
# Store the first price as buy_price
# Traverse through remaining prices
# Update buy_price if smaller value found
# Calculate profit using current_price - buy_price
# Store maximum profit
# Return profit

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

# Time Complexity  : O(n) — single pass through the array
# Space Complexity : O(1) — only two variables maintained