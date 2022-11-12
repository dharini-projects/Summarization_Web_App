

from crypt import methods
from urllib import request
from flask import Flask, render_template, url_for
from flask import request as req #req is used for communication between the front end and the back end
import requests

app = Flask(__name__,static_url_path="/static/css/main.css")
@app.route("/",methods = ["GET","POST"])
def Index():
    return(render_template("index.html"))

#invoke the following method if the 'Summarize' button is clicked in front end
@app.route("/get_summary",methods=["GET","POST"]) 
def get_summary():
    if req.method=="POST":
        # The authentication tokens to access the inference API
        API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
        headers = {"Authorization": f"Bearer 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"}

        #send the query to the model and get the response
        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()
            
        #input data has to be taken from 'form' in the front end
        #use the variable name 'input_text' given in the front end
        input_text = req.form["input_text"] 
        max_len = 100
        min_len = 20
        
        #load the query using the input text, minimum and maximum lengths of the summary
        output = query({
            "inputs": input_text,
            "parameters": {"min_length" : min_len, "max_length" : max_len},
        })[0]
        #return the summarized output 
        #use the variable names 'result' as given in the front end
        return render_template("index.html", result = output["summary_text"]) 
    else:
        return(render_template("index.html"))




if __name__ == '__main__':
    app.debug = True #should be true for testing, should be false for production
    app.run()



""" 

def Index():


    API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
    headers = {"Authorization": f"Bearer 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"}

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()
        
    data = '''The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building, 
    and the tallest structure in Paris. Its base is square, measuring 125 metres (410 ft) on each side. 
    During its construction, the Eiffel Tower surpassed the Washington Monument to become the tallest 
    man-made structure in the world, a title it held for 41 years until the Chrysler Building in New 
    York City was finished in 1930. It was the first structure to reach a height of 300 metres. Due 
    to the addition of a broadcasting aerial at the top of the tower in 1957, it is now taller than 
    the Chrysler Building by 5.2 metres (17 ft). Excluding transmitters, the Eiffel Tower is the second 
    tallest free-standing structure in France after the Millau Viaduct. '''

    minl = 30
    maxl = 70
    output = query({

        "inputs": data,
        "parameters": {"min_length" : minl, "max_length" : maxl},
    })

    return render_template("index.html", result = output, minlen = minl, maxlen = maxl)


#def hello():
#	return "Hello World!!!". """

