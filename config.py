import os

API_ID = API_ID = 28792498

API_HASH = os.environ.get("API_HASH", "7da2a29c9858ab0a2d00f48b8a68da2d)

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6698523764:AAGBJA9k--F_cgnNlvYVk0KLf-5x8F9FoHk)

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 7024777654))

LOG = -1002026204987

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5987970971").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


