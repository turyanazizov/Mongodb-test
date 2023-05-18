import pymongo

connection_url="mongodb://localhost:27017/"
client=pymongo.MongoClient(connection_url)
print("client: ",client)

database_name="employee_db"
employee_db=client[database_name]

collection_name='employee_details'
collection=employee_db[collection_name]

print("collection: ",employee_db.list_collection_names())
for c in collection.find():
    print(c)

"""Dokumente elave (insert) etmek"""
# 1. Yalniz bir elave ucun
document={"Name":"Abdul","Surname":"Aliyev","Emp_ID":"PY2023015","Position":"Data analyist","Country":"India"}
collection.insert_one(document)

# 2. Birden daha artiq elave ucun
documents=[
    {"Name":"Nizami","Surname":"Cafarov","Emp_ID":"PY2023006","Position":"Teacher","Country":"Azerbaijan"},
    {"Name":"Aga","Surname":"Agayev","Emp_ID":"PY2023007","Position":"React Developer","Country":"Azerbaijan"},
    {"Name":"Azer","Surname":"Aliyev","Emp_ID":"PY2023008","Position":"Devops","Country":"USA"}
]
collection.insert_many(documents)


"""Dokumentde axtaris (find) etmek"""
# 1. Yalniz bir axtaris neticesi ucun
query={"Name":"Aga"}
result=collection.find_one(query)
print("One result: ",result)


# 2. Birden daha artiq axtaris neticesi ucun
query={"Country":"Azerbaijan"}
result=collection.find(query)
print("Many result: ",result)
for r in result:
    print(r)


"""Dokumentde deyisiklik etmek"""
# 1. Yalniz bir deyisiklik ucun
query={"Emp_ID": {"$eq": "PY2023008"}}
present_data = collection.find_one(query)

new_data = {"$set": {"Name": "Abdul"}}
collection.update_one(present_data, new_data)

# 2. Birden daha artiq deyisiklik ucun
present_data = {"Branch": "Python Developer"}
new_data = {"$set": {"Branch": "Sr. Python Developer"}} 
collection.update_many (present_data, new_data)


"""Dokument silmek ucun"""
# 1. Yalniz bir silinme ucun
query={"Name":"Abdul"}
collection.delete_one(query)

# 2. Birden daha artiq silinme ucun
query={"Country":"Azeerbaijan"}
collection.delete_many(query)