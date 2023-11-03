from datetime import datetime
from datetime import timedelta
import math
from flask import request, copy_current_request_context
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from flask_restful import Resource
from flask_login import (current_user, login_user, logout_user, login_required)
import os
import requests
from config import ConfigClass

configclass = ConfigClass()

class VistaEmparejar(Resource):
    def post(self):
        
        profile = request.json            
        url_api_perfiles = f"{configclass.PERFILES_MS}/api/perfiles"
        response_api_perfiles = requests.post(url=url_api_perfiles, json=profile)                
        candidate_list = response_api_perfiles.json().get("candidatos")

        profile_detail = profile.get('profile')

        profile_skills = profile_detail['skills']
        profile_soft_skills = profile_detail['soft_skill']
        profile_psychological_skills = profile_detail['psychological']
        
        for i,candidate in enumerate(candidate_list):
            skills = candidate['skills']
            soft_skills = candidate['soft_skill']
            psychological_skills = candidate['psychological']

            count = 0
            sum = 0

            for skill in skills:
                if skill['id'] in profile_skills:
                    sum += skill['valoracion']
                    count += 1
            for skill in soft_skills:
                if skill['id'] in profile_soft_skills:
                    sum += skill['valoracion']
                    count += 1
            for skill in psychological_skills:
                if skill['id'] in profile_psychological_skills:
                    sum += skill['valoracion']
                    count += 1

            candidate_list[i]["calificacion"] = math.trunc(sum/count)
        filter_candidates=sorted(candidate_list, key=lambda i: i['calificacion'], reverse=True)

        return {"candidatos":filter_candidates}, 200  

def send_post_request(url, headers, body):
    #response = requests.post(url, json=body, headers=headers, timeout=5000)
    response = requests.post(url, json=body)
    return response.json()

def send_get_request(url, headers):
    response = requests.get(url=url, headers=headers, timeout=5000)
    return response.json()

class VistaPing(Resource):
    def get(self):
        print("pong")
        return {"Mensaje":"Pong"}, 200