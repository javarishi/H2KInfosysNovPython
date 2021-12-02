import os

path = "/RISHI/H2K/FileIO/DemoDec21.txt"
dir_path = "/RISHI/H2K/FileIO/new_dir_dec21"

if os.path.exists(path):
    print("This File already exists")
else:
    print("File Doesnt exist")


if os.path.exists(dir_path):
    print("Directory exists")
else:
    print("Creating new directory")
    os.mkdir(dir_path)

list_of_files = os.listdir("/RISHI/H2K/FileIO")
list_csv = []
for eachFile in list_of_files:
    if eachFile.count('teachers') > 0 :
        list_csv.append(eachFile)
        print(eachFile)

