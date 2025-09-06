import pandas as pd
import json
from kafka import KafkaProducer

def sp500_tickers():
    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    df = pd.read_html(url)[0]
    tickers = df['Symbol'].tolist()
    return tickers

def send_to_kafka():
    producer = KafkaProducer(
        bootstrap_servers='kafka:9092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

    producer.send(
        topic='sp500_tickers',
        value=sp500_tickers()
    )

    producer.flush()
    print("Tickers sent to Kafka.")

send_to_kafka()