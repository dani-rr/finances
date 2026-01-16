import pandas as pd
import json
from kafka import KafkaProducer
import requests
from io import StringIO
from config import KAFKA_BOOTSTRAP, TICKERS_TOPIC

def sp500_tickers(source_url, user_agent="Mozilla/5.0"):
    headers = {"User-Agent": user_agent}  # Pretend to be a browser
    response = requests.get(source_url, headers=headers, timeout=10)
    response.raise_for_status()  # raises an error if not 200 OK

    df = pd.read_html(StringIO(response.text))[0]
    return df['Symbol'].tolist()

def send_to_kafka(tickers, bootstrap_servers, topic):
    producer = KafkaProducer(
        bootstrap_servers=bootstrap_servers,
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

    producer.send(
        topic=topic,
        value=tickers
    )

    producer.flush()

def main():
    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    tickers = sp500_tickers(url)
    
    send_to_kafka(
        tickers=tickers,
        bootstrap_servers=KAFKA_BOOTSTRAP,
        topic=TICKERS_TOPIC,
    )
    
if __name__ == "__main__":
    main()    