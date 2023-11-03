import os
from dotenv import load_dotenv
load_dotenv()

class ConfigClass(object):
    PY_DB_NAME      =  os.getenv('PY_DB_NAME', '')
    PY_DB_USER      =  os.getenv('PY_DB_USER', '')
    PY_DB_PASS      =  os.getenv('PY_DB_PASS', '')
    PY_DB_HOST      =  os.getenv('PY_DB_HOST', '')
    PY_DB_PORT      =  os.getenv('PY_DB_PORT', '')

    HOST_ME_UNO     =  os.getenv('HOST_ME_UNO', '')
    HOST_ME_DOS     =  os.getenv('HOST_ME_DOS', '')
    HOST_ME_TRES    =  os.getenv('HOST_ME_TRES', '')
    HOST_PORT_UNO   =  os.getenv('HOST_PORT_UNO', '')
    HOST_PORT_DOS   =  os.getenv('HOST_PORT_DOS', '')
    HOST_PORT_TRES  =  os.getenv('HOST_PORT_TRES', '')