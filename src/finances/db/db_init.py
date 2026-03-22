import psycopg
import os
from finances.config import POSTGRES_HOST, POSTGRES_PORT, POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD

conn = psycopg.connect(
    host=POSTGRES_HOST,
    port=POSTGRES_PORT,
    dbname=POSTGRES_DB,
    user=POSTGRES_USER,
    password=POSTGRES_PASSWORD,
)


def init_stage() -> None:

    with conn.cursor() as cur:
        
        cur.execute("""
            CREATE SCHEMA IF NOT EXISTS stage                 
            """)
        
        cur.execute("""
                    CREATE TABLE IF NOT EXISTS stage.tickers_info (
                        kfk_topic varchar NOT NULL,
                        kfk_partition smallint NOT NULL,
                        kfk_offset bigint NOT NULL,
                        kfk_message varchar,
                        PRIMARY KEY (kfk_topic, kfk_partition, kfk_offset)                    
                    )
                    """)
        
        cur.execute("""
            CREATE TABLE IF NOT EXISTS stage.tickers_last_info (
                        kfk_topic varchar NOT NULL,
                        kfk_partition smallint NOT NULL,
                        kfk_offset bigint NOT NULL,
                        kfk_message varchar,
                        PRIMARY KEY (kfk_topic, kfk_partition, kfk_offset)                     
                    )
            """)
