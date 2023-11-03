from flask import Flask, request, jsonify
from flask_restful import Api
from vistas import ViewGetProfile, GetPing, GetLog

app = Flask(__name__)

app_context = app.app_context()
app_context.push()

api = Api(app)
api.add_resource(GetPing, '/api/validador/ping')
api.add_resource(ViewGetProfile, '/getprofile')


