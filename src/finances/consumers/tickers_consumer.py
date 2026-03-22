from finances.kafka.consumer_factory import build_json_consumer
from finances.kafka.readers import consume_latest
from finances.config import TICKERS_TOPIC
from finances.db.psql_conn import db_conn

conn = db_conn()

consumer = build_json_consumer(TICKERS_TOPIC, group_id="v2")


for message in consume_latest(consumer):
    
    with conn.cursor() as cur:
        
        cur.execute("""
                    INSERT INTO stage.tickers_info (
                        kfk_topic, 
                        kfk_partition, 
                        kfk_offset, 
                        kfk_message
                        )
                    VALUES (%s, %s, %s, %s)
                    """,
                    (
                    message.topic, 
                    message.partition,
                    message.offset,
                    str(message.value)
                    )
                    )
        consumer.commit()