# Importing the Required Library
import pywhatkit
import json

f = open('appsettings.json')
 
# returns JSON object as 
# a dictionary
data = json.load(f)

# Defining the Phone Number and Message
phone_number = data["phone_number"]
message = data["message"]

# Sending the WhatsApp Message
pywhatkit.sendwhatmsg_instantly(phone_number, message, 15, True, 4)


# Displaying a Success Message
print("WhatsApp message sent!")