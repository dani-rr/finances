import pandas as pd
import json
from kafka import KafkaProducer
import requests
from io import StringIO

def sp500_tickers():
    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    headers = {"User-Agent": "Mozilla/5.0"}  # Pretend to be a browser
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # raises an error if not 200 OK

    df = pd.read_html(StringIO(response.text))[0]
    tickers = df['Symbol'].tolist()
    tickers = ["try1400"]
    return tickers

def send_to_kafka():
    producer = KafkaProducer(
        bootstrap_servers='192.168.1.212:9092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

    producer.send(
        topic='sp500_tickers',
        value=sp500_tickers()
    )

    producer.flush()
    print("Tickers sent to Kafka.")

send_to_kafka()