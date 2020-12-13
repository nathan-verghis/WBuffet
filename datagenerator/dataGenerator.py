from alpha_vantage.timeseries import TimeSeries
import csv

"""
Generate market data for 5 different stocks
"""

userInput = input("Enter a Stock code (e.g. MSFT) to generate data for (q to exit): ")
while (userInput != "q"):
    dest = open("./dataGenerator/rawdata/" + userInput + ".csv", 'a')
    writer = csv.writer(dest)
    ts = TimeSeries(key='OBHHBPMPB779VWRM', output_format='csv')
    data, metadata = ts.get_intraday(symbol=userInput, interval='1min', outputsize='full')
    for row in data:
        writer.writerow(row)
    
    dest.close()
    userInput = input("\nEnter a Stock to generate data for (q to exit): ")

exit(1)
dest = open('./dataGenerator/rawdata/data1.csv', 'a')

writer = csv.writer(dest)
ts = TimeSeries(key='OBHHBPMPB779VWRM', output_format='csv')
data, metadata = ts.get_intraday(symbol='MSFT', interval='1min', outputsize='full')
for row in data:
    writer.writerow(row)
    
dest.close()

dest = open('./dataGenerator/rawdata/data2.csv', 'a')

writer = csv.writer(dest)
ts = TimeSeries(key='OBHHBPMPB779VWRM', output_format='csv')
data, metadata = ts.get_intraday(symbol='OLED', interval='1min', outputsize='full')
for row in data:
    writer.writerow(row)
    
dest.close()

dest = open('./dataGenerator/rawdata/data3.csv', 'a')

writer = csv.writer(dest)
ts = TimeSeries(key='OBHHBPMPB779VWRM', output_format='csv')
data, metadata = ts.get_intraday(symbol='EQ', interval='1min', outputsize='full')
for row in data:
    writer.writerow(row)
    
dest.close()

dest = open('./dataGenerator/rawdata/data4.csv', 'a')

writer = csv.writer(dest)
ts = TimeSeries(key='OBHHBPMPB779VWRM', output_format='csv')
data, metadata = ts.get_intraday(symbol='NIO', interval='1min', outputsize='full')
for row in data:
    writer.writerow(row)
    
dest.close()

dest = open('./dataGenerator/rawdata/data5.csv', 'a')

writer = csv.writer(dest)
ts = TimeSeries(key='OBHHBPMPB779VWRM', output_format='csv')
data, metadata = ts.get_intraday(symbol='BE', interval='1min', outputsize='full')
for row in data:
    writer.writerow(row)
    
dest.close()


