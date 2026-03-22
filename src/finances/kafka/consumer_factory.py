from kafka import KafkaConsumer
import json
from finances.config  import KAFKA_BOOTSTRAP

def build_json_consumer(topic: str, group_id: str) -> KafkaConsumer:
    return KafkaConsumer(
        topic,
        group_id=group_id,
        bootstrap_servers=[KAFKA_BOOTSTRAP],
        auto_offset_reset="earliest",
        value_deserializer=lambda m: json.loads(m.decode('ascii')),
        consumer_timeout_ms=1000
        )