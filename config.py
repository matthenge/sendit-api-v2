import os

class Config():
    """The main configuration class"""
    DEBUG = False
    TESTING = False
    SECRET_KEY = "james"
    DBNAME = "sendit"
    DBUSER = "postgres"
    DBHOST = "localhost"
    DBPASS = "james"

class DevtConfiguration(Config):
    """The development configuration class"""
    DEBUG = True
    DB_URL = "dbname='sendit'  user='postgres' password='james' host='localhost'"

class ProdConfiguration(Config):
    """The production configuration"""
    DB_URL = os.getenv("DB_URL")
    SECRET_KEY = os.getenv("SECRET_KEY")    

class TestConfiguration(Config):
    DEBUG = True
    DBNAME = "sendit_test"
    DBUSER = "postgres"
    DBHOST = "localhost"
    DBPASS = "james"
    DB_URL = "dbname='sendit_test'  user='postgres' password='james' host='localhost'"

configuration = {
    "devt": DevtConfiguration,
    "prod": ProdConfiguration,
    "test": TestConfiguration
}