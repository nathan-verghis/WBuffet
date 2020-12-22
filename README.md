An AI to predict the stock market using linear regression.

Now I know this sounds too good to be true. My theory behind the potential success of using linear regression is that I'm, hoping this bot will
be able to replicate the process when using Candlestick Methods. Most candlestick patterns range from 3 - 4 increments of data, my algorithm will be 
trained from 10. This should mean if my baseline assumptions are correct, that not only will it be able to look at these patterns to determine a trigger 
point of puchases, but also as a context.

CURRENTLY IN DEVELOPMENT

After testing phase (6 - 8 months working on live market data, analysis on decided trades to evaluate %P / %L), bot will be released live if passed

3 Step Process :

    1: Fet the daily trending stocks

    2: From 9:30AM - 11:10AM (API limits to 500 calls per day, 5 stocks X 100 X 1 min intervals)
    collect market data and feed into algorithm

    3: Make predictions about the closing values of those 10 stocks 1 min into future. Based on these
    predictions buy and sell longs/shorts to profit

Current Issues:
    
    1: I'm using the AlphaVantage stock API to make my calls and retrieve market data. Being in the testing/training phase, I'm not concerned with how 
    accurate the data is, however I find that even when I make calls for 1 minute interval data, there are missing entries in the data. This could prove
    disastrous as it may train my network on false patterns, and may require a different API to be used.

    2: AI issue. Design is flawed and its nothing a few good hours on stack overflow can't fix.
    