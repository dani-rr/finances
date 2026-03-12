import json
import yfinance as yf
from kafka import KafkaProducer

from finances.config import KAFKA_BOOTSTRAP, TICKERS_LAST_INFO_TOPIC
from finances.producers.tickers_producer import sp500_tickers
import pandas as pd

def get_tickers_last_info(tickers):
    df = yf.download(
        tickers,
        period="1d",
        interval="5m",
        rounding=False,
        group_by="ticker",  # keeps a consistent MultiIndex when multiple tickers
    )

    if df is None or df.empty:
        return {}

    last_row = df.iloc[-1]
    return last_row_to_json(last_row)

def last_row_to_json(last_row):

    ts = last_row.name  # usually pandas.Timestamp

    if hasattr(last_row.index, "levels"):  # MultiIndex columns
        data = (
            last_row
            .unstack()
            .to_dict(orient="index")
        )
        return {
            "timestamp": ts.isoformat() if hasattr(ts, "isoformat") else str(ts),
            "data": data,
        }


def send_to_kafka(payload, bootstrap_servers, topic):
    producer = KafkaProducer(
        bootstrap_servers=bootstrap_servers,
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    )
    producer.send(topic=topic, value=payload)
    producer.flush()
    
def main():
    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    tickers = sp500_tickers(url)
    payload = get_tickers_last_info(tickers)
    send_to_kafka(payload, KAFKA_BOOTSTRAP, TICKERS_LAST_INFO_TOPIC)

if __name__ == "__main__":
    main()    