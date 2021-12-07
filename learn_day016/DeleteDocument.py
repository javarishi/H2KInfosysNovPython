import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
test_database = myclient["testdatabase_dec2021"]
new_collection = test_database["store_collection"]

myquery = { "store_number": "0111" }

x = new_collection.delete_one(myquery)
print(x.deleted_count)

myclient.close()