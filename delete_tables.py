from db_connection import PostgresConnection
from connection_params import CONNECTION_PARAMS, CLIENT_TABLE, QUEUE_TABLE


PostgresConnection(CONNECTION_PARAMS).run_cmd(
    'DROP TABLE %s; DROP TABLE %s;' % (CLIENT_TABLE, QUEUE_TABLE)
)