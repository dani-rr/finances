from kafka import KafkaConsumer
import json
from finances.config import KAFKA_BOOTSTRAP, TICKERS_LAST_INFO_TOPIC
# import msgpack
# from kafka import KafkaConsumer, TopicPartition
# import logging
# logging.basicConfig(level=logging.DEBUG)
# logging.getLogger("kafka").setLevel(logging.DEBUG)


# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer(TICKERS_LAST_INFO_TOPIC,
                         group_id='v2',
                         bootstrap_servers=[KAFKA_BOOTSTRAP],
                         auto_offset_reset='earliest',
                         enable_auto_commit=True,
                         value_deserializer=lambda m: json.loads(m.decode('ascii')),
                         consumer_timeout_ms=1000)


for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))
    consumer.commit()
    
