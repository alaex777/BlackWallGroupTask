# Blask Wall Group task
## API for transaction
### Initialization
1. docker compose up
2. python3 -m venv venv
3. source venv/bin/activate
4. pip install -r requirements.txt
5. docker compose up
6. python3 db_utils/create_tables.py
7. python3 db_utils/fill_clients.py
### Run app
uvicorn main:app --reload
### Use app
Get request on ```localhost:8000/transfer/<sender_id>/<receiver_id>/<amount>```