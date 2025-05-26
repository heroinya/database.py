import time
import json
import os

database = {}
user_id = 1

while True:
    user_login = input(f"Enter the login for user {user_id}: ")
    user_password1 = input(f"Enter the password for user {user_id}: ")
    user_password2 = input(f"Enter again the password for user {user_id}: ")

    if user_password1 != user_password2:
        print(" ")
        print("Password check failed, the program will restart in 5 seconds")
        print(" ")
        time.sleep(5)
        continue

    database[f"user_{user_id}"] = {
        "login": user_login,
        "password": user_password1,
    }

    user_id += 1
    cont = input("Do you want to add another user? (yes/no): ")
    if cont.lower() != "yes":
        break

print(" ")
for user in database:
    print(f"{user} login: {database[user]['login']}")
    print(f"{user} password: {database[user]['password']}")
    print(" ")

export_data = input("Do you want to export data to a file? (yes/no): ")
if export_data.lower() == "yes":
    filename = "database.json"
    if os.path.exists(filename):
        print("File already exists. Data will be appended to the existing file.")
        with open(filename, "r") as file:
            existing_data = json.load(file)
            existing_user_ids = [int(user.split("_")[1]) for user in existing_data]
            max_user_id = max(existing_user_ids)
            for user in database:
                user_id = max_user_id + 1
                existing_data[f"user_{user_id}"] = database[user]
                max_user_id += 1
        with open(filename, "w") as file:
            json.dump(existing_data, file, indent=4)
    else:
        with open(filename, "w") as file:
            json.dump(database, file, indent=4)
    print("Data has been exported to", filename)
else:
    print("Data will not be exported.")
