import psycopg
from finances.config import POSTGRES_HOST, POSTGRES_PORT, POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD

def db_conn(
    host : str = POSTGRES_HOST,
    port: str = POSTGRES_PORT,
    dbname: str = POSTGRES_DB,
    user : str = POSTGRES_USER,
    password : str = POSTGRES_PASSWORD
            ):
    
    return psycopg.connect(
                            host=POSTGRES_HOST,
                            port=POSTGRES_PORT,
                            dbname=POSTGRES_DB,
                            user=POSTGRES_USER,
                            password=POSTGRES_PASSWORD,
                        )
