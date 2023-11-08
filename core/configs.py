from pydantic.v1 import BaseSettings
from sqlalchemy.orm import declarative_base

class Settings(BaseSettings):
    """
        Configurações gerais utilizadas em nossa aplicação
    """
    API_V1_STR: str = '/api/v1' #não precisa inserir via hard coding
    DB_URL: str = 'mysql+asyncmy://root@127.0.0.1:3306/etscursos' #ideal seria
    #user: password
    DBBaseModel = declarative_base() #serve para que os models herdem todos os recursos do sqlalchemy
    class Config:
        case_sensitive = True

settings = Settings() #declarando a variável aqui, em qualquer lugar que eu
#importar o arquivo terei acesso a essas configurações.