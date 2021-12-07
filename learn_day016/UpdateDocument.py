import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
test_database = myclient["testdatabase_dec2021"]
new_collection = test_database["store_collection"]

myquery = { "store_number": "0141" }
newvalues = { "$set": { "store_name": "Perimeter Blvd" , "address" : "141 Perimeter Blvd"} }

x = new_collection.update_one(myquery, newvalues)
print(x.modified_count)


myclient.close()