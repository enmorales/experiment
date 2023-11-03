from flask import Flask, request, jsonify
from flask_restful import Api
from vistas import VistaPing, VistaEmparejar

# from motoremp_ms import create_app
# from motoremp_ms.vistas.vistas import VistaPing, VistaEmparejar
# from flask_restful import Api

# app=create_app('default')

app = Flask(__name__)

app_context=app.app_context()
app_context.push()

api = Api(app)
api.add_resource(VistaEmparejar, '/motor/emparejar')
api.add_resource(VistaPing, '/motor/ping')