path = "/RISHI/H2K/FileIO/DemoDec21.txt"
# w - write
# a - append
# x - create
test_file = open(path, 'a')
for i in range(1,10):
    test_file.write("This is Line Number {}".format(i))
    test_file.write("\n")
test_file.close()