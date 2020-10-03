import streamlit as st
import requests
import main_functions


#st.write("Entering requestArticles...")
# our API key in a variable
apiKeyDict = main_functions.read_from_file("JSON_documents/myAPIKey.json")
myApiKey = apiKeyDict["myKey"]

def save_response(url, fileName):

    #st.write("Entering saveResponse function...")
    response = requests.get(url).json()
    main_functions.save_to_file(response, "JSON_documents/" + fileName)

# for part 1 - get the user requested topic
def get_topics(topic):

    #st.write("Entering getTopics function...")
   # st.write("P1:", topic)

    urlForTopic = "https://api.nytimes.com/svc/topstories/v2/" + topic + ".json?api-key=" + myApiKey
    save_response(urlForTopic, "topicResults.json")

# for part 2 - get the user requested shareAction and timeframe
def get_popular(share_action, time_frame):

    # If user wants to see most shared then you'll need to append "facebook" to the URL
    # otherwise, let the facebook var exist as an empty string
    facebook_share = ""
    if share_action == "Most emailed":
        share_action = "emailed"
    elif share_action == "Most shared":
        share_action = "shared"
        facebook_share = "/facebook"
    else:
        share_action = "viewed"

    if time_frame == "1 Day":
        time_frame = "1"
    elif time_frame == "7 Days":
        time_frame = "7"
    else:
        time_frame = "30"

    #st.write("share_action:", share_action)
    #st.write("time_frame:", time_frame)

    #emailed - shared - viewed / 1 - 7 - 30
    urlForPopularity = "https://api.nytimes.com/svc/mostpopular/v2/" + share_action + "/" + time_frame + facebook_share + ".json?api-key=" + myApiKey
    save_response(urlForPopularity, "popularResults.json")