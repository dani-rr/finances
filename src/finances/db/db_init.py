from finances.db.psql_conn import db_conn


def init_stage() -> None:
    conn = db_conn()
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


if __name__ == "__main__":
    init_stage()