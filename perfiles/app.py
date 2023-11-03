from flask import Flask
from flask_restful import Api
from vistas import ProfileView, PingView

app = Flask(__name__)

app_context = app.app_context()
app_context.push()

api = Api(app)
api.add_resource(PingView, '/api/perfiles/ping')
api.add_resource(ProfileView, '/api/perfiles')