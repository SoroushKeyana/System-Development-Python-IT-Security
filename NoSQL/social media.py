import pymongo
from datetime import datetime


client = pymongo.MongoClient("localhost", 27017)
db = client['social_media']
user_collection = db['users']
post_collection = db['posts']

#Registering the user here
def user_registration(email, username, password, status=False):
    detail = {
        "email": email,
        "username": username,
        "password": password,
        "status": status,
        "following": []
    }
    user = user_collection.find_one({"$or": [{"email": email, "username": username}]})
    if user:
        print("Username or email already exist")
    else:
        user_collection.insert_one(detail)
        print(f"Welcome {username} please log in")

#User log in
def user_log_in(username, password):
    user = user_collection.find_one({"username":username, "password":password})

    if user:
        print(f"You are logged in {username}")
        user_collection.update_one({"username": username}, {"$set":{"status": True}})
    else:
        print(f"Wrong username or password")
        print(f"If you are new please create account")

#User can post if he/she is logged in
def user_post(username, message):
    user = user_collection.find_one({'username': username})
    status = user.get("status")
    post = {
        "username": username,
        "message": message,
        "timestamp": datetime.now()
    }
    if status:
        post_collection.insert_one(post)
        print("You successfully posted something")
    else:
        print("please log in first to be able to post")

#User can follow users
def follow_user(username, target_username):
    target = user_collection.find_one({'username': target_username})

    if target:
        user_collection.update_one({"username": username},{"$addToSet":{"following": target_username}})
        print(f"You followed {target_username}")
    else:
        print("The user doesn't exist")
#user can unfollow unsers
def unfollow_user(username, target_username):
    target = user_collection.find_one({'username': target_username})

    if target:
        user_collection.update_one({"username": username},{"$pull":{"following": target_username}})
        print(f"You unfollowed {target_username}")
    else:
        print("The user doesn't exist")

#view uesr feeds
def view_user_feed(username, target_username):
    user = user_collection.find_one({'username': username})
    posts = post_collection.find({'username': target_username})

    if user and 'following' in user and isinstance(user['following'], list) and target_username in user['following']:
        for post in posts:
            message = post.get("message")
            print(message)
    else:
        print("You are not following this person.")

#user_registration('someyehfaizi@gmail.com', 'Samya', '123')
#user_log_in("Samya",'123')
#user_post('Barsam', 'Stop carpet bombing Gaza!')
#follow_user("Samya", "Barsam")

view_user_feed("Samya", "Erik") 