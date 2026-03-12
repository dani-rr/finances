import psycopg

with psycopg.connect("dbname=finances user=finances") as conn:
    
    with conn.cursor() as cur:
        
        cur.execute("""
                    CREATE TABLE stage.tickers_info (
                        kfk_partition PRIMARY KEY,
                        kfk_offset PRIMARY KEY,
                        
                    )
                    """)