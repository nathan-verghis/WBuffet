import csv


"""
Modify data to place the target prediction in the next column
"""

# remove empty rows
def remove_empty_rows(filename):
    data = []
    filesrc = './dataGenerator/rawdata/' + filename
    filedest = './dataGenerator/mod_data/' + filename

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
def combine(filename):
    data = []
    filesrc = './dataGenerator/mod_data/' + filename
    filedest = './dataGenerator/mod_data/dataFinal.csv'

    # read data into list
    with open(filesrc, 'r') as src:
        reader = csv.reader(src)
        for row in reader:
            data.append(row)

    # copy list into dest
    with open(filedest, 'a') as dest:
        writer = csv.writer(dest, lineterminator = '\n')
        writer.writerows(data)

def removeTimeStamp(filename):
    data = []
    filesrc = './dataGenerator/mod_data/' + filename
    filedest = './dataGenerator/mod_data/'+ filename
    
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
        data[0].append("open" + str(i + 1) + ",high" + str(i + 1) + ",low" + str(i + 1) + ",close" + str(i + 1) + ",volume" + str(i + 1) + "")

    # copy list into dest
    with open(filedest, 'w') as dest:
        writer = csv.writer(dest, lineterminator = '\n')
        writer.writerows(data)



# remove the empty rows from the files
remove_empty_rows('data1.csv')
remove_empty_rows('data2.csv')
remove_empty_rows('data3.csv')
remove_empty_rows('data4.csv')
remove_empty_rows('data5.csv')

# combine data into one datafile
"""combine('data1.csv')
combine('data2.csv')
combine('data3.csv')
combine('data4.csv')
combine('data5.csv')"""

removeTimeStamp("data1.csv")
removeTimeStamp("data2.csv")
removeTimeStamp("data3.csv")
removeTimeStamp("data4.csv")
removeTimeStamp("data5.csv")