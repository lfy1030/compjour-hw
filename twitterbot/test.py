import twit_utils
# assuming you have a creds file named "~/Desktop/tw.json"
CREDS_FILE = "~/Desktop/tw.json"
api = twit_utils.get_api(CREDS_FILE)
obj = api.me()
print("My name is", obj.screen_name)