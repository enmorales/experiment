# FROM python:3.10

# RUN mkdir /proyecto1
# RUN cd /proyecto1
# RUN mkdir motoremp_ms
# RUN cd motoremp_ms

# WORKDIR /proyecto1/motoremp_ms
# COPY . /proyecto1/motoremp_ms

# RUN pip install -r requirements.txt

# WORKDIR /proyecto1

FROM python:3.10-slim-buster

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip 

RUN pip install -r requirements.txt

# ENV CONTAINER=SI
# ENV POSTGRES_URL=postgresql+psycopg2://admin:admin@candidatosdb:5432/CandidatosDB

ENV FLASK_APP=app.py

EXPOSE 5000

# CMD ["gunicorn", "--bind", "0.0.0.0:5005", "motoremp_ms.wsgi:app"]

CMD ["python", "-m" , "flask" ,"run", "--host=0.0.0.0"]


#COPY ./requirements.txt /app/requirements.txt
#COPY ./app.py /app/app.py
#COPY ./test_offers.py /app/test_offers.py
#COPY ./wsgi.py /app/wsgi.py
#COPY ./run.sh /app/run.sh

#WORKDIR /app

#RUN pip install -r requirements.txt

#ENV PORT=5003
#ENV SECRET_KEY=nativa2023

#CMD ["gunicorn", "--bind", "0.0.0.0:5003", "wsgi:app"]


## Empezar corriendo una imagen de python 
#FROM python:3.8-alpine

## Copiar requerimientos para ejecutar el programa
#COPY ./requirements.txt /app/requirements.txt

## Cambiar de directorio de trabajo a donde esta el ejectuable del API
#WORKDIR /app

## Instalar requerimientos de la app
#RUN pip install -r requirements.txt

## Copiar el contenido del directorio actual en la imagen de docker
#COPY . /app

## Agregar variable de entorno con el nombre del estudiante
#ENV user_name Estudiante

## Variable de entorno para escribir en txt dentro de la contenedora el resultado
## Por defecto esta en false (No escribe txt en la contenedora)
#ENV write_result not_show

## Configurar el contenedor para correr en una manera ejectuble
#ENTRYPOINT [ "python" ]

## Archivo principal donde corre el API
#CMD ["view.py" ]


#FROM python:3.8.3 
#ENV PYTHONUNBUFFERED 1 
#RUN apt-getupdate && apt-getinstall -y gdal-bin
#COPY ./requirements.txt .
#RUN pipinstall -r requirements.txt 
#RUN mkdir /code | mkdir /scripts 
#WORKDIR /code
#COPY ./src . 
#CMD ["python", "manage.py", "start" ]