import apiai

CLIENT_ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN_HERE'



def parse_dialogflow():
	request = ai.text_request()
    request.query = user_text
 
    # Receiving the response.
    response = json.loads(request.getresponse().read().decode('utf-8'))
    responseStatus = response['status']['code']
    if (responseStatus == 200):
        # Sending the textual response of the bot.
        return (response['result']['fulfillment']['speech'])
 
    else:
        return ("Sorry, I don't have a response for that yet")
	