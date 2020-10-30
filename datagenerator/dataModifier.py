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



# remove the empty rows from the files
remove_empty_rows('data1.csv')
remove_empty_rows('data2.csv')
remove_empty_rows('data3.csv')
remove_empty_rows('data4.csv')
remove_empty_rows('data5.csv')