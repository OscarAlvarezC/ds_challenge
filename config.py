import os
import pymysql
pymysql.install_as_MySQLdb()

class Config:
    pass

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = f"mysql://root:{os.getenv('MYSQL_PASS')}@localhost/rappi" 
    # using other database engines
    #'sqlite:///' + os.path.join(basedir, 'database.db')
    # postgresql://username:password@host:port/database_name
    # mysql://username:password@host:port/database_name
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}