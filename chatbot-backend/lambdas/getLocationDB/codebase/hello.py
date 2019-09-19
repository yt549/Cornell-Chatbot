'''Function that remember user's "name" and greet the user with "name" '''


def hello(event, context):
    # name = event["currentIntent"]["slots"]["Name"].title()
    name = event["currentIntent"]["slots"]["Name"].title()
    response = {
        "dialogAction":
            {
                "type": "Close",
                "fulfillmentState": "Fulfilled",
                "message":
                    {
                        "contentType": "PlainText",
                        "content": "Hi " + name + ". Cornell welcomes you!"
                    }
            }
    }
    return response

# test
# def hello(event, context):
#     intent = event["currentIntent"]["name"]
#
#     invocationSource = event["invocationSource"]
#
#
#     if intent == "hello":
#         name = event["currentIntent"]["slots"]["Name"].title()
#         sessionAttributes = event["sessionAttributes"]
#         response = {
#             "sessionAttributes":
#                 {
#                     "Name": name,
#                     "invocationSource": invocationSource
#                 },
#             "dialogAction":
#                 {
#                     "type": "Close",
#                     "fulfillmentState": "Fulfilled",
#                     "message":
#                         {
#                             "contentType": "PlainText",
#                             "content": "Hi " + name + ". Cornell welcomes you!!!"
#                         }
#                 }
#         }
#     elif intent == "beforeHello":
#         if "Name" in sessionAttributes:
#             response = {
#                 "dialogAction":
#                     {
#                         "type": "ElicitSlot",
#                         "message":
#                             {
#                               "contentType": "PlainText",
#                               "content": "change to get location intent"
#                             },
#                        "intentName": "getLocation",
#                        "slots":
#                            {
#                               "CornellLocation": null
#                            },
#                        "slotToElicit" : "CornellLocation"
#                     }
#
#             }
#         else:
#             response = {
#                 "dialogAction":
#                     {
#                         "type": "ElicitSlot",
#                         "message":
#                             {
#                               "contentType": "PlainText",
#                               "content": "change to asking name"
#                             },
#                        "intentName": "hello",
#                        "slots":
#                            {
#                               "Name": null
#                            },
#                        "slotToElicit" : "Name"
#                     }
#
#             }
        # response = {
        #     "sessionAttributes":
        #         {
        #             "invocationSource": invocationSource
        #         },
        #     "dialogAction":
        #         {
        #             "type": "Close",
        #             "fulfillmentState": "Fulfilled",
        #             "message":
        #                 {
        #                     "contentType": "PlainText",
        #                     "content": "Hi beforeHello"
        #                 }
        #         }
        # }



    return response
