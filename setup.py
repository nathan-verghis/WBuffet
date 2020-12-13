from datagenerator.dataGenerator import generate
from webscraper.TopFive import TrendingTickers
from datagenerator.dataModifier import remove_empty_rows
from datagenerator.dataModifier import removeTimeStamp
from datagenerator.dataModifier import combine
from datetime import date
import os

today = date.today().strftime("%b-%d-%Y")
print("Getting today's trenders...")
scanner = TrendingTickers()
scanner.start()
data = scanner.getData()
print("Got the trenders! Here they are:")

# see the trenders for today
print(data, today)
today = "testing"

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
userInput = input("Press '1' if data is for testing or '0' if data is for training: ")

if userInput == 1:
    today = "testing"
elif userInput == 0:
    today = "training"

# create files both raw and modified
for stocks in data:
    remove_empty_rows(stocks, today)
    removeTimeStamp(stocks, today)
    combine(stocks, today)
print("Successfully Generated Data!")
