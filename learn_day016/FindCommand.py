import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
test_database = myclient["testdatabase_dec2021"]
new_collection = test_database["store_collection"]

docu_selector = { "store_number": "0141" }
field_selector = {"_id": 0, 'store_number' : 1, 'store_name': 1}
many_myquery = { "store_number": { "$gt": "01" } }

record = new_collection.find_one(docu_selector, field_selector)
print(record)

for eachDoc in new_collection.find(many_myquery, field_selector):
    print(eachDoc)


myclient.close()

