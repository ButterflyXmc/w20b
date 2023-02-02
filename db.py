import mariadb
import dbcreds

# * CONNECTING TO THE DB
def connect_to_db():
    try:
        conn = mariadb.connect(
                                        user = dbcreds.user,
                                        password = dbcreds.password,
                                        host = dbcreds.host,
                                        port = dbcreds.port,
                                        database = dbcreds.database,
                                        autocommit = True
            )
        cursor = conn.cursor()
        return cursor
    except mariadb.OperationalError as error:
            print("!__!Operational error! Not able to connect to the database!__!", error)
    except Exception as error:
            print("!__!Something went wrong!__!", error)

# * Cursor
def cursor(conn):
    return conn.cursor()

# * Close Cursor
def close_cursor(cursor):
    cursor.close()

# * Close Connection
def close_conn(conn):
    conn.close()
