from flask import request
from flask_restful import Resource
from config import ConfigClass
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

configclass = ConfigClass()

# Configura la conexión a la base de datos PostgreSQL
engine = create_engine('postgresql://tu_usuario:tu_contraseña@localhost:tu_base_de_datos')

# Crea una sesión
Session = sessionmaker(bind=engine)
session = Session()

# Crea la base para definir las clases de las tablas
Base = declarative_base()

# Definición de las clases de las tablas (las clases ya están definidas en el código anterior)

class ProfileView(Resource):
        
    def post(self):
        # Realiza la consulta para obtener todos los candidatos y sus habilidades
        candidatos_con_habilidades = session.query(PerfilCandidato).all()
        
        # Crea la lista de candidatos en formato JSON
        candidatos_json = []
        for candidato in candidatos_con_habilidades:
            candidato_json = {
                "id": candidato.id,
                "full_name": "",  # Agrega el nombre del candidato si lo tienes
                "skills": [{"id": habilidad.idHabilidadTecnica, "valoracion": 50} for habilidad in candidato.habilidades_tecnicas],
                "soft_skill": [{"id": habilidad.idHabilidadBlanda, "valoracion": 60} for habilidad in candidato.habilidades_blandas],
                "psychological": [{"id": rasgo.idRasgoPersonalidad, "valoracion": 70} for rasgo in candidato.rasgos_personalidad]
            }
            candidatos_json.append(candidato_json)

        return {'candidatos': candidatos_json}, 200

# Cierra la sesión
session.close()
