from alpha_vantage.timeseries import TimeSeries
import csv

"""
Generate market data for 5 different stocks
"""


def generate(names, date):
    for name in names:
        dest = open("./datalogs/" + date + "/rawdata/" + name + ".csv", 'a')
        writer = csv.writer(dest)
        ts = TimeSeries(key='OBHHBPMPB779VWRM', output_format='csv')
        data, metadata = ts.get_intraday(symbol=name, interval='1min', outputsize='full')
        for row in data:
            writer.writerow(row)
            
        dest.close()



if __name__ == "__main__":    
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

