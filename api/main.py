from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
import openai


app = Flask(__name__)
CORS(app)  # Enable CORS for the entire app
api = Api(app)
API_KEY = os.environ.get('API_KEY')
openai.api_key = API_KEY


def promptInput(userInput):
    trainingMessages = [
        {"role": "system", "content": "You are a podcaster who helps turn textbook and news article inputs, and possibly other inputs into digestible, moderately entertaining, and comprehensive shortform solo podcasts. Your content will be immediately fed into a text to speech generator which will then be outputted to students around the country, so please ensure that you have high quality and also nothing outside of content which should be read alound"},
        {"role": "user", "content": """ 
     With the text in brackets([]) below create the podcast that aligns with previous instructions:
    [
     Like most scientific disciplines, fluid mechanics has a history of erratically occurring
early achievements, then an intermediate era of steady fundamental discoveries in the
eighteenth and nineteenth centuries, leading to the twenty-first-century era of “modern
practice,” as we self-centeredly term our limited but up-to-date knowledge. Ancient
civilizations had enough knowledge to solve certain flow problems. Sailing ships with
oars and irrigation systems were both known in prehistoric times. The Greeks produced quantitative information. Archimedes and Hero of Alexandria both postulated
the parallelogram law for addition of vectors in the third century B.C. Archimedes
(285–212 B.C.) formulated the laws of buoyancy and applied them to floating and submerged bodies, actually deriving a form of the differential calculus as part of the
analysis. The Romans built extensive aqueduct systems in the fourth century B.C. but
left no records showing any quantitative knowledge of design principles.
From the birth of Christ to the Renaissance there was a steady improvement in the
design of such flow systems as ships and canals and water conduits but no recorded
evidence of fundamental improvements in flow analysis. Then Leonardo da Vinci
(1452–1519) stated the equation of conservation of mass in one-dimensional steady
flow. Leonardo was an excellent experimentalist, and his notes contain accurate
descriptions of waves, jets, hydraulic jumps, eddy formation, and both low-drag
(streamlined) and high-drag (parachute) designs. A Frenchman, Edme Mariotte
(1620–1684), built the first wind tunnel and tested models in it.
Problems involving the momentum of fluids could finally be analyzed after Isaac
Newton (1642–1727) postulated his laws of motion and the law of viscosity of the linear fluids now called newtonian. The theory first yielded to the assumption of a “perfect” or frictionless fluid, and eighteenth-century mathematicians (Daniel Bernoulli,
Leonhard Euler, Jean d’Alembert, Joseph-Louis Lagrange, and Pierre-Simon Laplace)
produced many beautiful solutions of frictionless-flow problems. Euler, Fig. 1.1, developed both the differential equations of motion and their integrated form, now called
the Bernoulli equation. D’Alembert used them to show his famous paradox: that a body
immersed in a frictionless fluid has zero drag. These beautiful results amounted to
overkill, since perfect-fluid assumptions have very limited application in practice and
most engineering flows are dominated by the effects of viscosity. Engineers began to
reject what they regarded as a totally unrealistic theory and developed the science of
hydraulics, relying almost entirely on experiment. Such experimentalists as Chézy,
Pitot, Borda, Weber, Francis, Hagen, Poiseuille, Darcy, Manning, Bazin, and Weisbach
produced data on a variety of flows such as open channels, ship resistance, pipe flows,
waves, and turbines. All too often the data were used in raw form without regard to
the fundamental physics of flow
    ] 
"""},
        {"role": "assistant", "content": """

Welcome back to another episode of "Fluid Insights," the podcast where we dive into the fascinating world of fluid mechanics, breaking down the complexities into bite-sized, easily digestible pieces.

Like many scientific disciplines, fluid mechanics has a rich history marked by early achievements, steady discoveries, and the modern practices we rely on today. Our story begins in ancient civilizations, where sailing ships, irrigation systems, and basic flow problems were already being addressed.

The Greeks, in the third century B.C., contributed quantitative knowledge to the field. Archimedes and Hero of Alexandria proposed the parallelogram law for vector addition, with Archimedes even formulating the laws of buoyancy and delving into a form of differential calculus.

Fast forward to the Renaissance, and we meet the polymath Leonardo da Vinci, who not only improved the design of flow systems but also stated the equation of conservation of mass in one-dimensional steady flow. His experimental prowess left us with accurate descriptions of waves, jets, hydraulic jumps, and various designs.

Edme Mariotte, a Frenchman in the 17th century, took things a step further by building the first wind tunnel and testing models in it. Momentum analysis became possible after Isaac Newton's laws of motion and viscosity entered the scene.

The 18th-century mathematicians, including Daniel Bernoulli, Leonhard Euler, Jean d’Alembert, Joseph-Louis Lagrange, and Pierre-Simon Laplace, produced beautiful solutions to frictionless-flow problems. Euler, in particular, developed the famous Bernoulli equation.

However, this perfect-fluid assumption had limited practical application, leading engineers to embrace the science of hydraulics. Chézy, Pitot, Borda, Weber, Francis, Hagen, Poiseuille, Darcy, Manning, Bazin, and Weisbach emerged as influential experimentalists, producing data on open channels, ship resistance, pipe flows, waves, and turbines.

Unfortunately, engineers sometimes used this data without considering the fundamental physics of flow, as the effects of viscosity often dominate real-world engineering scenarios.

And that, dear listeners, brings us to the end of our journey through the historical currents of fluid mechanics. From ancient civilizations to the experimentalists of the 18th and 19th centuries, each wave has contributed to the ocean of knowledge we navigate today.

Thank you for joining me on this episode of "Fluid Insights." Until next time, stay curious and go with the flow!

"""},
        {"role": "user", "content": "input"},


    ]


class Summarization(Resource):
    def get(self):
        pass

    def post(self):
        data = request.get_json()
        content = data[content]

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=promptInput(content)

        )
        print(response['choices'][0]['message']['content'])
        pass


# api.add_resource(TextToSpeech, '/tts')
api.add_resources(Summarization, "/summarize")

if __name__ == '__main__':
    app.run(debug=True)
