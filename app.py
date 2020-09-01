from flask import Flask, request, jsonify # Imports the flask library modules
app = Flask(__name__) # Single module that grabs all modules executing from this file
app.config['JSON_SORT_KEYS'] = False

@app.route('/login', methods=['GET', 'POST']) # HTTP request methods namely "GET" or "POST"
def login():
    data = []
    if request.method == 'POST': # Checks if it's a POST request
        data = [dict(id='1', name='max', email='max@gmail.com')] # Data structure of JSON format
        response = jsonify(data) # Converts your data strcuture into JSON format
        response.status_code = 202 # Provides a response status code of 202 which is "Accepted"

        return response # Returns the HTTP response
    else:
        data = [dict(id='none777', name='none', enmail='none')] # Data structure of JSON format
        response = jsonify(data) # Converts your data strcuture into JSON format
        response.status_code = 406 # Provides a response status code of 406 which is "Not Acceptable"

        return response # Returns the HTTP response

@app.route('/getprediction', methods=['GET', 'POST']) # HTTP request methods namely "GET" or "POST"
def getprediction():
    data = []
    if request.method == 'POST': # Checks if it's a POST request
        data = [dict(id='1', name='max', email='max@gmail.com')] # Data structure of JSON format
        response = jsonify(data) # Converts your data strcuture into JSON format
        response.status_code = 202 # Provides a response status code of 202 which is "Accepted"

        return response # Returns the HTTP response
    else:
        data = [dict(id='none777', name='none', enmail='none')] # Data structure of JSON format
        comedy_entry = {'id': 'MOVIEID',
                        'movie_name': 'MOVIENAME',
                        'time': 'TIME',
                        'channel': 'movie_channel'}
        nesjson = {
                      "Customer Name":"Pranav Singh",
                      "Phone":"(404)-353-5436",
                      "Mailing Address": "1000 Towncenter way suite #210,canonnonsburg,PENNSYLVANIA, 15317",
                      "Call History" : [
                                        {
                                         "Event-Date" : "11/04/2019",
                                         "Event-Description": "Channel(chat) callback requested",
                                         "Event-Experience" : 50
                                         },
                                          {
                                              "Event-Date": "10/29/2019",
                                              "Event-Description": "Channel(Voice) Billing Inquiry",
                                              "Event-Experience": 30
                                          },
                                          {
                                              "Event-Date": "10/19/2019",
                                              "Event-Description": "Channel(Voice) Billing Inquiry",
                                              "Event-Experience": 30
                                          },
                                          {
                                              "Event-Date": "07/22/2019",
                                              "Event-Description": "Channel(Voice) Service Issues",
                                              "Event-Experience": 30
                                          }
                                        ],
                                "Sentiment analysis": [
                                    {
                                        "Experience": "Medium",
                                        "Event-Score": 50
                                    }
                                ],
                            "Churn Score": [
                                {
                                    "Experience": "Medium",
                                    "Event-Score": 65
                                }
                            ],
                      "RECOMMENDED NEXT BEST ACTIONS": {
                        "1.":"Reverse a month's charge",
                        "2.": "Move the customer to the Unlimited data plan"
                      },
                    "Predicted reason for call": "Seeking resolution ongoing dispute"
                     }

        response = jsonify(nesjson) # Converts your data strcuture into JSON format
        response.status_code = 406 # Provides a response status code of 406 which is "Not Acceptable"

        return response # Returns the HTTP response

