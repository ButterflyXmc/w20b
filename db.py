import mariadb
import dbcreds

# * CONNECTING TO THE DB
# def connect_to_db():
#     try:
#         conn = mariadb.connect(
#                                         user = dbcreds.user,
#                                         password = dbcreds.password,
#                                         host = dbcreds.host,
#                                         port = dbcreds.port,
#                                         database = dbcreds.database,
#                                         # autocommit = True
#             )
#     except mariadb.OperationalError as error:
#             print("Operational error!", error)
#     except Exception as error:
#             print("Something went wrong!", error)
#             return None

# * Cursor
def cursor(conn):
    return conn.cursor()

# * Close Cursor
def close_cursor(cursor):
    cursor.close()

# * Close Connection
def close_conn(conn):
    conn.close()
