from kafka import KafkaConsumer, TopicPartition
from finances.config import KAFKA_BOOTSTRAP, TICKERS_LAST_INFO_TOPIC

print("BOOTSTRAP:", KAFKA_BOOTSTRAP)
print("TOPIC:", TICKERS_LAST_INFO_TOPIC)

c = KafkaConsumer(bootstrap_servers=KAFKA_BOOTSTRAP, consumer_timeout_ms=5000)
print("connected:", c.bootstrap_connected())
print("known topics contains target:", TICKERS_LAST_INFO_TOPIC in c.topics())

parts = c.partitions_for_topic(TICKERS_LAST_INFO_TOPIC)
print("partitions:", parts)

if not parts:
    print("No partitions found for topic on this broker.")
else:
    tps = [TopicPartition(TICKERS_LAST_INFO_TOPIC, p) for p in parts]
    c.assign(tps)  # bypass group issues for debugging
    beg = c.beginning_offsets(tps)
    end = c.end_offsets(tps)
    print("beginning:", beg)
    print("end:", end)

    for tp in tps:
        c.seek(tp, max(beg[tp], end[tp] - 2))  # read last 2 messages

    for msg in c:
        print(msg.topic, msg.partition, msg.offset, msg.value.decode("utf-8"))