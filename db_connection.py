from typing import Optional

import psycopg2 as psql


class DBConnectionParameters():
    dbname: str
    user: str
    password: str
    host: str
    port: str

    def __init__(self, dbname, user, password, host, port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port


class PostgresConnection():
    def __init__(self, connection_params: DBConnectionParameters):
        self.__connection_params = connection_params

    def run_cmd(self, cmd: str) -> Optional[str]:
        conn = psql.connect(dbname=self.__connection_params.dbname,
                            user=self.__connection_params.user,
                            password=self.__connection_params.password,
                            host=self.__connection_params.host,
                            port=self.__connection_params.port,
                            )
        cursor = conn.cursor()
        cursor.execute(cmd)

        try:
            records = cursor.fetchall()
        except:
            records = []

        cursor.close()
        conn.close()

        if len(records) == 0:
            return None
        if len(records) > 1:
            raise Exception('Too many objects')
        return records[0][0]
