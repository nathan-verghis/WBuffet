from alpha_vantage.timeseries import TimeSeries
import csv

"""
Generate market data for 5 different stocks
"""


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


