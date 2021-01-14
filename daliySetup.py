from datagenerator.dataGenerator import generate
from webscraper.TopFive import TrendingTickers
from datagenerator.dataModifier import remove_empty_rows
from datagenerator.dataModifier import removeTimeStamp
from datagenerator.dataModifier import combine
from datagenerator.dataModifier import targetModifier
from datetime import date
import os
import csv

def dailySetup():

    today = date.today().strftime("%b-%d-%Y")
    print("Getting today's trenders...")
    scanner = TrendingTickers()
    scanner.start()
    data = scanner.getData()
    print("Got the trenders! Here they are:")

    # see the trenders for today
    print(data, today)

    # create directories
    try:
        os.mkdir("./datalogs/" + today)
        os.mkdir("./datalogs/" + today + "/rawdata")
        os.mkdir("./datalogs/" + today + "/mod_data")
    except OSError:
        print("Unable to make directory")
        exit(1)

    # create raw data
    print("Generating raw data...")
    generate(data, today)

    # only to be used during testing
    '''userInput = input("Press '1' if data is for testing or '0' if data is for training: ")

    if userInput == 1:
        today = "testing"
    elif userInput == 0:
        today = "training"'''

    # create files both raw and modified
    with open("./datalogs/" + today + "/dataFinal.csv", 'w') as dest:
            writer = csv.writer(dest, lineterminator = '\n')
            info = []
            for i in range(10):
                info.append("open" + str(i + 1))
                info.append("high" + str(i + 1))
                info.append("low" + str(i + 1))
                info.append("close" + str(i + 1))
                info.append("volume" + str(i + 1))
            info.append("target")
            writer.writerow(info)
    for stocks in data:
        remove_empty_rows(stocks, today)
        removeTimeStamp(stocks, today)
        combine(stocks, today)
        targetModifier(today, stocks)
    print("Successfully Generated Data!")
