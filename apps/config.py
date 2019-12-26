DB = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = 'root'
HOST = '127.0.0.1'
PORT = 3306
DB_NAME = 'flask_1226'
CHARSET = 'utf8'

SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset={}'.format(DB, DRIVER, USERNAME, PASSWORD, HOST, PORT, DB_NAME,
                                                                     CHARSET)
SQLALCHEMY_TRACK_MODIFICATIONS = False
