from fastapi import FastAPI

from db_connection import PostgresConnection
from connection_params import CLIENT_TABLE, QUEUE_TABLE, CONNECTION_PARAMS


app = FastAPI()

@app.get('transfer/{sender_id}/{receiver_id}/{amount}')
def transfer(sender_id: str, receiver_id: str, amount: int):
    postgres_connection = PostgresConnection(CONNECTION_PARAMS)

    try:
        if postgres_connection.run_cmd(
            'SELECT balance FROM %s WHERE client_id = %s' % 
            (CLIENT_TABLE, sender_id)
        ) < amount:
            return {'error': 'not enough balance'}
    except:
        return {'error': 'can`t connect to postgres or process the statement'}

    cmd = 'BEGIN'
    transfer_cmd = 'UPDATE clients SET '
    transfer_cmd += '' % ()
