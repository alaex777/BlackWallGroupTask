import sys

sys.path.append('../BlackWallGroupTask')

from db_connection import PostgresConnection
from connection_params import CONNECTION_PARAMS, CLIENT_TABLE


connection = PostgresConnection(CONNECTION_PARAMS)
for i in range(1, 10):
    connection.run_cmd(
        'INSERT INTO %s VALUES (%s, %s);' % 
        (CLIENT_TABLE, str(i), str(i*100))
    )
