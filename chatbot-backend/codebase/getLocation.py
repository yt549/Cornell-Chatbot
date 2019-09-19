'''Function that remember user's "name" and greet the user with "name" '''

from geopy.geocoders import Nominatim


def getLocation(event, context):
    geolocator = Nominatim(user_agent="specify_your_app_name_here")

    loc = event["currentIntent"]["slots"]["CornellLocation"]
    location = geolocator.geocode(loc)
    addr = location.address
    response = {
        "dialogAction":
            {
                "type": "Close",
                "fulfillmentState": "Fulfilled",
                "message":
                    {
                        "contentType": "PlainText",
                        "content": "This is your location: " + addr
                    }
            }
    }
    return response

#
# geolocator = Nominatim(user_agent="specify_your_app_name_here")
# # location = geolocator.geocode("174 5th Avenue NYC")
# location = geolocator.geocode("Olin Library Ithaca")
# addr = location.address
# print(addr)
