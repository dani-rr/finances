from finances.kafka.consumer_factory import build_json_consumer
from finances.kafka.readers import consume_all
from finances.config import TICKERS_TOPIC

consumer = build_json_consumer(TICKERS_TOPIC, group_id="v2")


for message in consume_all(consumer):
    print ("%s;%d;%d;%s;%s" % (message.topic, 
                               message.partition,
                               message.offset,
                               message.key,
                               message.value))
    consumer.commit()