from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
import openai


app = Flask(__name__)
CORS(app)  # Enable CORS for the entire app
api = Api(app)
API_KEY = os.environ.get('API_KEY')
openai.api_key = API_KEY


trainingMessages = [
    {"role": "system", "content": "what we need it to do"},
    {"role": "user", "content": "what user wants to say"},
    {"role": "assistant", "content": "GPT's response"},

]


class Summarization(Resource):
    def get(self):
        pass

    def post(self):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=trainingMessages

        )
        print(response['choices'][0]['message']['content'])
        pass


# api.add_resource(TextToSpeech, '/tts')
api.add_resources(Summarization, "/summarize")

if __name__ == '__main__':
    app.run(debug=True)
