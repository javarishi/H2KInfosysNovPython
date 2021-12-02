# Open - file --> Path mode - r, w, a kind of file - t
path = "/RISHI/H2K/FileIO/CSVTest.csv"
test_file = open(path, 'rt')
# Read
#print(test_file.read())
for eachLine in test_file:
    itemList = eachLine.split(',')
    for eachItem in itemList:
        print(eachItem)
# close
test_file.close()



