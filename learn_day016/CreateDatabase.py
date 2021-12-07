import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
test_database = myclient["testdatabase_dec2021"]
new_collection = test_database["store_collection"]

oneStore = {
    "_id" : "0239218378213",
    "store_number": "0111",
    "store_name": "Duluth Parkway",
    "address": "0111 Duluth Pwky"
}
mylist = [
    { "store_number": "0141", "store_name": "Perimeter Circle", "address": "141 Perimeter Circle" },
    { "store_number": "0131", "store_name": "Spring Hill", "address": "131 Spring Hill Pkwy" }
]
x =  new_collection.insert_one(oneStore)
# x = new_collection.insert_many(mylist)

print("Done!", x.inserted_id)
myclient.close()
