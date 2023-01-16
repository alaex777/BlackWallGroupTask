from db_connection import PostgresConnection
from connection_params import CONNECTION_PARAMS, CLIENT_TABLE, QUEUE_TABLE


connection = PostgresConnection(CONNECTION_PARAMS)

connection.run_cmd(
    'CREATE TABLE %s (ClientId int, Balance int);' % (CLIENT_TABLE)
    
)
connection.run_cmd(
    'CREATE TABLE %s (SenderId int, ReceiverId int, Balance int);' % (QUEUE_TABLE)
)