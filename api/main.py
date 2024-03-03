from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_cors import CORS
from openai import OpenAI
import os
from trainingData import promptInput
app = Flask(__name__)
CORS(app)  # Enable CORS for the entire app
api = Api(app)

client = OpenAI(api_key="env var")


class Summarization(Resource):
    def get(self):
        pass

    def post(self):
        data = request.get_json()

        preference = data["setting"]
        # prompt getting fed into message

        finalPrompt = f"create a podcast based off of {preference}, and with the system instructions"

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
