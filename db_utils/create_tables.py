import sys

sys.path.append('../BlackWallGroupTask')

from db_connection import PostgresConnection
from connection_params import CONNECTION_PARAMS, CLIENT_TABLE, QUEUE_TABLE


connection = PostgresConnection(CONNECTION_PARAMS)

connection.run_cmd(
    'CREATE TABLE %s (client_id int, balance int);' % (CLIENT_TABLE)
)
connection.run_cmd(
    'CREATE TABLE %s (sender_id int, receiver_id int, balance int);' % 
    (QUEUE_TABLE)
)
