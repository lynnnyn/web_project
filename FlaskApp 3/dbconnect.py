import pymysql

def connection():
    conn = pymysql.connect(host="localhost",
                           user = "root",
                           passwd = "root",
                           db = "foooooodie_program")
    c = conn.cursor()

    return c, conn
