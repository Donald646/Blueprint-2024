from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_cors import CORS
from openai import OpenAI
import os
from trainingData import promptInput
app = Flask(__name__)
CORS(app)  # Enable CORS for the entire app
api = Api(app)
API_KEY = ""  # put api key here
client = OpenAI(api_key=API_KEY)


class Summarization(Resource):
    def get(self):
        pass

    def post(self):
        data = request.get_json()
        content = data["content"]
        setting = data["setting"]
        # prompt getting fed into message
        if setting == "podcast":
            finalPrompt = f"create a podcast that aligns with the system instructions. [{content}]"
        elif setting == "summarize":
            finalPrompt = f"Summarize the text in the brackets into small digestible chunks that encapsulate the main idea and relavent details.[{content}]"

        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=promptInput(finalPrompt)
        )
        print("completion", completion)
        GPTresponse = completion.choices[0].message.content

        return {"response": GPTresponse}


# api.add_resource(TextToSpeech, '/tts')
api.add_resource(Summarization, "/summarize")

if __name__ == '__main__':
    app.run(debug=True)
