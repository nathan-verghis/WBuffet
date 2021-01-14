import csv


"""
Modify data to place the target prediction in the next column
"""

def bushFix(date, filename):
    data = []
    beginnings = []
    filesrc = './datalogs/' + date + '/' + filename
    filedest = './datalogs/' + date + '/(1)' + filename
    
    # read data into list
    with open(filesrc, 'r') as src:
        reader = csv.reader(src)
        for row in reader:
            data.append(row)

    # get beginnings
    for row in range(len(data)):
        if row != 0:
            beginnings.append(float(data[row][0]))
        else:
            beginnings.append(None)


    # store goal at the end of each line of data
    for row in range(len(data)):
        if row != 0:
            if float(data[row][-1]) > beginnings[row]:
                data[row][-1] = '2'
            if float(data[row][-1]) < beginnings[row]:
                data[row][-1] = '1'
            if float(data[row][-1]) == beginnings[row]:
                data[row][-1] = '0'

    # copy list into dest
    with open(filedest, 'w') as dest:
        writer = csv.writer(dest, lineterminator = '\n')
        writer.writerows(data)


if __name__ == "__main__":

    # further modification
    bushFix("Jan-13-2021", 'dataFinal.csv')
    bushFix("Dec-18-2020", 'dataFinal.csv')
    bushFix("Dec-15-2020", 'dataFinal.csv')