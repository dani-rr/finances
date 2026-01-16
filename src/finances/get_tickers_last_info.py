import json
import yfinance as yf
from kafka import KafkaProducer

from finances.config import KAFKA_BOOTSTRAP, TICKERS_LAST_INFO_TOPIC
from finances.get_tickers import sp500_tickers
import pandas as pd

def get_tickers_last_info(tickers):
    df = yf.download(
        tickers,
        period="1d",
        interval="15m",
        rounding=False,
        group_by="ticker",  # keeps a consistent MultiIndex when multiple tickers
    )

    if df is None or df.empty:
        return {}

    last_row = df.iloc[-1]
    return last_row_to_json(last_row)

def last_row_to_json(last_row):
    # Coerce numpy types to native Python for JSON safety
    def to_native(value):
        if hasattr(value, "item"):
            return value.item()
        return value

    if hasattr(last_row.index, "levels"):  # MultiIndex columns
        swapped = last_row.swaplevel().sort_index()
        return {
            ticker: {k: to_native(v) for k, v in fields.to_dict().items()}
            for ticker, fields in swapped.groupby(level=0)
        }

    # Single-ticker case: columns are simple Index
    return {k: to_native(v) for k, v in last_row.to_dict().items()}

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