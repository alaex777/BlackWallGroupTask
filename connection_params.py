from db_connection import DBConnectionParameters


CONNECTION_PARAMS = DBConnectionParameters(
    dbname='bwg_db',
    user='bwg_user',
    password='bwg_password',
    host='localhost',
    port='5432'
)

CLIENT_TABLE = 'clients'
QUEUE_TABLE = 'queue'
