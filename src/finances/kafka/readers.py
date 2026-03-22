def consume_all(consumer):
    for message in consumer:
        yield message
        
def consume_latest(consumer):
    consumer.poll(timeout_ms=100)
    consumer.seek_to_end()
    for message in consumer:
        yield message