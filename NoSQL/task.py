import pymongo 
# Connect to MongoDB 
client = pymongo.MongoClient("mongodb://localhost:27017/") 
database = client["mydb"]
collection = database["tasks"] 
def add_task(title, description, status="To Do"): 
    document = {"title": title, "description": description, "status": status}
    collection.insert_one(document) 

def list_tasks(): 
    cursor = collection.find()
    for document in cursor:
        print(document) 

def update_task_status(task_id, new_status): 
    collection.update_one({"title": task_id},{"$set": {"status": new_status}}) 

def delete_task(task_id): 
    collection.delete_one({"title": task_id})

list_tasks()