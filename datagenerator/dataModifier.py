import csv


"""
Modify data to place the target prediction in the next column
"""

# remove empty rows
def remove_empty_rows(filename, date):
    data = []
    filesrc = './datalogs/' + date + '/rawdata/' + filename + ".csv"
    filedest = './datalogs/' + date + '/mod_data/' + filename + ".csv"

    # read data into list
    with open(filesrc, 'r') as src:
        reader = csv.reader(src)
        for row in reader:
            if row != []:
                data.append(row)

    # write to destination
    with open(filedest, 'w') as dest:
        writer = csv.writer(dest, lineterminator='\n')
        writer.writerows(data)

# add data to one dataset
def combine(filename, date):
    data = []
    filesrc = './datalogs/' + date + '/mod_data/' + filename + ".csv"
    filedest = './datalogs/' + date + '/dataFinal.csv'

    # read data into list
    with open(filesrc, 'r') as src:
        reader = csv.reader(src)
        for row in reader:
            data.append(row)
    
    # remove labels
    data.remove(data[0])

    # copy list into dest
    with open(filedest, 'a') as dest:
        writer = csv.writer(dest, lineterminator = '\n')
        writer.writerows(data)

def removeTimeStamp(filename, date):
    data = []
    filesrc = './datalogs/' + date + '/mod_data/' + filename + ".csv"
    filedest = './datalogs/' + date + '/mod_data/'+ filename + ".csv"
    
    # read data into list
    with open(filesrc, 'r') as src:
        reader = csv.reader(src)
        for row in reader:
            data.append(row)

    # remove time stamp
    for row in range(len(data)):
        data[row].remove(data[row][0])

    # align the previous 9 minutes into 1 line
    for row in range(len(data)):
        if row < len(data) - 10 and row != 0:
            for i in range(9):
                data[row].extend(data[row + 1 + i])

    # remove last lines
    data = data[:-10]

    # store goal at the end of each line of data
    for row in range(len(data)):
        if row != 0 or row != 1:
            data[row].append(data[row - 1][0])

    # remove first entry as training/testing target unavailable
    data.remove(data[1])

    # edit labels
    data[0] = []
    for i in range(10):
        data[0].append("open" + str(i + 1))
        data[0].append("high" + str(i + 1))
        data[0].append("low" + str(i + 1))
        data[0].append("close" + str(i + 1))
        data[0].append("volume" + str(i + 1))
    data[0].append("target")

    # copy list into dest
    with open(filedest, 'w') as dest:
        writer = csv.writer(dest, lineterminator = '\n')
        writer.writerows(data)


if __name__ == "__main__":
    # remove the empty rows from the files
    remove_empty_rows('data1', 'testing')
    remove_empty_rows('data2', 'testing')
    remove_empty_rows('data3', 'testing')
    remove_empty_rows('data4', 'testing')
    remove_empty_rows('data5', 'testing')

    # further modification
    removeTimeStamp("data1", 'testing')
    removeTimeStamp("data2", 'testing')
    removeTimeStamp("data3", 'testing')
    removeTimeStamp("data4", 'testing')
    removeTimeStamp("data5", 'testing')

    # combine data into one datafile
    with open("./dataGenerator/mod_data/dataFinal.csv", 'w') as dest:
        writer = csv.writer(dest, lineterminator = '\n')
        data = []
        for i in range(10):
            data.append("open" + str(i + 1))
            data.append("high" + str(i + 1))
            data.append("low" + str(i + 1))
            data.append("close" + str(i + 1))
            data.append("volume" + str(i + 1))
        data.append("target")
        writer.writerow(data)
    combine('data1', 'testing')
    combine('data2', 'testing')
    combine('data3', 'testing')
    combine('data4', 'testing')
    combine('data5', 'testing')