import js
import os 
import requests

import pyodide_http

# Patch the Requests library so it works with Pyscript
pyodide_http.patch_all()

OPENAI_API_KEY = "YOUR_API_KEY"

url = "https://api.openai.com/v1/chat/completions"
headers = {"Content-Type": "application/json",
           "Authorization": f"Bearer {OPENAI_API_KEY}"}
def send():

    user_mood = js.document.getElementById('mood')  # selecting element using id attribute
    mood_value = user_mood.value  # getting value of selected option

    #print(mood_value)
    
# chat gtp messages will be stored here
    messages = [

        {"role": "system",
         "content": "You are a kind helpful assistant"}
    ]

    if mood_value:
        message = f"I'm feeling {mood_value}, please give me a short encouraging affirmation"

    

    # if there is a message we append the new message from the user (you)
    if message:
        messages.append({"role": "user", "content": message})
        data = {"model": "gpt-3.5-turbo", "messages": messages}
    
        response = requests.post(url, headers=headers, json=data)
    
        reply = response.json()["choices"][0]["message"]["content"]

    print("\n" + reply + "\n")
