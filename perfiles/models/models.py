from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class PerfilCandidato(Base):
    __tablename__ = 'PerfilCandidato'

    id = Column(Integer, primary_key=True)
    idCandidato = Column(Integer)
    curriculum = Column(String)
    descripcion = Column(String)

    habilidades_tecnicas = relationship('PerfilCandidatoHabilidadTecnica')
    habilidades_blandas = relationship('PerfilCandidatoHabilidadBlanda')
    rasgos_personalidad = relationship('PerfilCandidatoRasgoPersonalidad')

    def as_dict(self):
        return {
            'id': self.id,
            'idCandidato': self.idCandidato,
            'curriculum': self.curriculum,
            'descripcion': self.descripcion,
            'habilidades_tecnicas': [hab.idHabilidadTecnica for hab in self.habilidades_tecnicas],
            'habilidades_blandas': [hab.idHabilidadBlanda for hab in self.habilidades_blandas],
            'rasgos_personalidad': [ras.idRasgoPersonalidad for ras in self.rasgos_personalidad]
        }

class PerfilCandidatoHabilidadTecnica(Base):
    __tablename__ = 'PerfilCandidatoHabilidadTecnica'

    id = Column(Integer, primary_key=True)
    idPerfilCandidato = Column(Integer, ForeignKey('PerfilCandidato.id'))
    idHabilidadTecnica = Column(Integer, ForeignKey('HabilidadTecnica.id'))

class PerfilCandidatoHabilidadBlanda(Base):
    __tablename__ = 'PerfilCandidatoHabilidadBlanda'

    id = Column(Integer, primary_key=True)
    idPerfilCandidato = Column(Integer, ForeignKey('PerfilCandidato.id'))
    idHabilidadBlanda = Column(Integer, ForeignKey('HabilidadBlanda.id'))

class PerfilCandidatoRasgoPersonalidad(Base):
    __tablename__ = 'PerfilCandidatoRasgoPersonalidad'

    id = Column(Integer, primary_key=True)
    idPerfilCandidato = Column(Integer, ForeignKey('PerfilCandidato.id'))
    idRasgoPersonalidad = Column(Integer, ForeignKey('RasgoPersonalidad.id'))