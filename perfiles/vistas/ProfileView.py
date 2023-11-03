import os
from flask import request
from flask_restful import Resource
from models.database import session
from models import PerfilCandidato, PerfilCandidatoHabilidadTecnica, PerfilCandidatoHabilidadBlanda, PerfilCandidatoRasgoPersonalidad 
from sqlalchemy import or_
from sqlalchemy.orm import aliased
import random
import redis
import json

class ProfileView(Resource):    
    
    def post(self):        
        redis_host = os.environ.get("REDIS_HOST", "localhost")
        redis_port = os.environ.get("REDIS_PORT", 6379)
        redis_password = os.environ.get("REDIS_PASSWORD", None)
        redis_client = redis.Redis(host=redis_host, port=redis_port, password=redis_password)
        redis_expire = os.environ.get("REDIS_EXPIRE", 300000)
        profile = request.json.get('profile')
       
        habilidades_tecnicas_alias = aliased(PerfilCandidatoHabilidadTecnica)
        habilidades_blandas_alias = aliased(PerfilCandidatoHabilidadBlanda)
        rasgos_personalidad_alias = aliased(PerfilCandidatoRasgoPersonalidad)
    
        data = []
        data_from = random.randint(1, 10)
        profiles_json_string = redis_client.get('profile')
        if data_from > 2 and profiles_json_string:
            data_from = "redis"
            data = json.loads(profiles_json_string.decode('utf-8'))
        else:
            data_from = "database"
            candidatos_con_habilidades = session.query(PerfilCandidato).join(habilidades_tecnicas_alias).join(habilidades_blandas_alias).join(rasgos_personalidad_alias).filter(
                or_(
                    habilidades_tecnicas_alias.idHabilidadTecnica.in_(profile['skills']),
                    habilidades_blandas_alias.idHabilidadBlanda.in_(profile['soft_skill']),
                    rasgos_personalidad_alias.idRasgoPersonalidad.in_(profile['psychological'])        
            )).all()
            
            for candidato in candidatos_con_habilidades:
                candidato_data = {
                    'id': candidato.id,
                    'full_name': str(candidato.id),
                    'curriculum': candidato.curriculum,
                    'descripcion': candidato.descripcion,
                    'skills': [{"id": hab.idHabilidadTecnica, "valoracion": 70 } for hab in candidato.habilidades_tecnicas],
                    'soft_skill': [{"id": hab.idHabilidadBlanda,"valoracion": 60} for hab in candidato.habilidades_blandas],
                    'psychological': [{"id": ras.idRasgoPersonalidad, "valoracion": 80}  for ras in candidato.rasgos_personalidad]
                }
                data.append(candidato_data)

                if not profiles_json_string:                    
                    redis_client.set('profile',  json.dumps(data))
                    redis_client.pexpire('profile', redis_expire)

        return {'candidatos': data, 'totalCount': len(data), 'tipo_consulta': data_from}, 200