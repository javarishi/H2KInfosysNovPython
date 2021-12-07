import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
list_databases = myclient.list_database_names()
for eachDB in list_databases:
    print(eachDB)

test_database = myclient["testdatabase"]
list_collections = test_database.list_collection_names()
print("###### Collection Names #####")
for eachCollection in list_collections:
    print("Collection: ", eachCollection)












myclient.close()