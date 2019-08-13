# 数据库参数配置
DIALCT = "mysql"
DRIVER = "pymysql"
USERNAME = "root"
PASSWORD = "admin123"
HOST = "127.0.0.1"
PORT = "3306"
DATABASE = "mysql"
# MYSQL
MYSQL_DB_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(
    DIALCT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)

SQLALCHEMY_DATABASE_URI = MYSQL_DB_URI
SQLALCHEMY_ECHO = True
