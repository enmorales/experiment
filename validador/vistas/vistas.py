from flask import request, jsonify, json
import requests 
from flask_restful import Resource
import os
import concurrent.futures
from config import ConfigClass
import datetime

configclass = ConfigClass()
list_error = []
num_solicitud = 0

class GetPing(Resource):
    def get(self):
        return {'message': "pong"}, 200

class GetLog(Resource):
    def get(self):
        return list_error, 200

class ViewGetProfile(Resource):
    def post(self):
        global num_solicitud
        num_solicitud +=  1    
        profile = request.json
        ruta_endpoint = 'motor/emparejar'

        solicitudes = [
            (f"{configclass.HOST_ME_UNO}:{configclass.HOST_PORT_UNO}/{ruta_endpoint}", profile),
            (f"{configclass.HOST_ME_DOS}:{configclass.HOST_PORT_DOS}/{ruta_endpoint}", profile),
            (f"{configclass.HOST_ME_TRES}:{configclass.HOST_PORT_TRES}/{ruta_endpoint}", profile)
            ]

        num_hilos = 3 
        num_intentos = 3

        with concurrent.futures.ThreadPoolExecutor(max_workers=num_hilos) as executor:
            resultados = list(executor.map(lambda args: self.thread_function(*args), solicitudes))

        # Si tenemos 100% los tres son iguales
        if self.list_compare(resultados[0], resultados[1]) and self.list_compare(resultados[0], resultados[2]): 
            self.reg_log(num_solicitud, 0, 0)
            return {'message': resultados[0], 'nivel_precision': '99%'}, 200
        
        # Si tenemos 66.66%, ms 3 falla
        if (resultados[0] == resultados[1]) and (resultados[0] != resultados[2]):
            i = 0
            while i < num_intentos and resultados[2] != resultados[0] :
                resultados[2] = self.thread_function(f"{configclass.HOST_ME_TRES}:{configclass.HOST_PORT_TRES}/{ruta_endpoint}", profile)
                i = i+1

            #list_error.append({'microservice': 3, 'intento': i})
            self.reg_log(num_solicitud, 3, i)

            return {'message': resultados[0], 'nivel_precision': '66%'}, 201
        
        # Si tenemos 66.66%, ms 2 falla
        if (resultados[0] == resultados[2]) and (resultados[0] != resultados[1]):
            i = 0

            while i < num_intentos and resultados[1] != resultados[0] :
                resultados[1] = self.thread_function(f"{configclass.HOST_ME_DOS}:{configclass.HOST_PORT_DOS}/{ruta_endpoint}", profile)
                i = i+1

            self.reg_log(num_solicitud, 2, i)

            return {'message': resultados[0], 'nivel_precision': '66%'}, 201
        
        # Si tenemos 66.66%, ms 1 falla
        if (resultados[1] == resultados[2]) and (resultados[0] != resultados[1]):
            i = 0

            while i < num_intentos and resultados[0] != resultados[1] :
                resultados[0] = self.thread_function(f"{configclass.HOST_ME_UNO}:{configclass.HOST_PORT_UNO}/{ruta_endpoint}", profile)
                i = i+1

            self.reg_log(num_solicitud, 1, i)

            return {'message': resultados[1], 'nivel_precision': '66%'}, 201
        
        # Si tenemos 0% los tres son diferentes retornarmos solo los elementos que coincidan
        if (resultados[0] != resultados[1]) and (resultados[0] != resultados[2]):
            claves_comunes = set()
            if resultados[0]:
                 claves_comunes.update(resultados[0].keys())
            if resultados[1]:
                 claves_comunes.update(resultados[1].keys())
            if resultados[2]:
                 claves_comunes.update(resultados[2].keys())
            
            diccionario_comun = {clave: resultados[0][clave] for clave in claves_comunes}
            return {'message': diccionario_comun, 'nivel_precision': '0%'}, 202

        return {'message': None, 'nivel_precision': '0%'}, 404
    
    def reg_log(self, num_sol, microservice, num_intento ):
        fecha_hora_actual = datetime.datetime.now()
        fecha_hora_como_cadena = fecha_hora_actual.strftime("%Y-%m-%d;%H:%M:%S")

        with open('log_procesamiento.txt', 'a') as f:
            label = 'Error'
            if num_intento == 0:
                label = 'Success'
            f.write(f"{fecha_hora_como_cadena};{num_sol};{microservice};{num_intento};{label}")
            f.write('\n')

    def reconect_microservice (self, url, profile):
        num_intentos = 3
        i = 0       
        res = None
        while i < num_intentos and res == None :
            res = self.thread_function(url, profile)
            i = i+1

        return {'num_reintento': i, 'resultado': res}

    def list_compare(self, list_one, list_two):
        if list_one == list_two:
            return True
        
        return False

    def thread_function(self, url, profile):
        try:
            response = requests.post(url, json = profile)
            if response.status_code == 200:
                return response.json()
            else:
                return []
        except:
            return []

        