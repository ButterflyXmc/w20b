import mariadb
import dbcreds


conn = mariadb.connect(
                            user = dbcreds.user,
                            password = dbcreds.password,
                            host = dbcreds.host,
                            port = dbcreds.port,
                            database = dbcreds.database,
                            autocommit = True
                            )
cursor = conn.cursor()