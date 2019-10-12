from hubspot3 import Hubspot3
import os
from dotenv import load_dotenv
load_dotenv()

### HubSpot ###
API_KEY = os.getenv("API_KEY")
client = Hubspot3(api_key=API_KEY)

firstname = "Testy"
lastname = "Buster"
email = "testybuster@gmail.com"
phone = "873-273-8734"

data = {
    "properties": [
        {
            "property": "firstname",
            "value": f"{firstname}"
        },
        {
            "property": "lastname",
            "value": f"{lastname}"
        },
        {
            "property": "email",
            "value": f"{email}"
        },
        {
            "property": "phone",
            "value": f"{phone}"
        }
    ]
}
# call this on a button press from a flask app
# contact = client.contacts.create(data=data)

