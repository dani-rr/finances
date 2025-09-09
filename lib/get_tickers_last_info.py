import yfinance as yf
from kafka import KafkaProducer
import json
import get_tickers

def get_tickers_last_info(tickers):
    tickers_info_df = yf.download(tickers, period='1d', interval='15m', rounding=False, multi_level_index=False)
    tickers_last_info_df = tickers_info_df.iloc[-1]
    tickers_last_info_json = last_row_to_json(tickers_last_info_df)
    return tickers_last_info_json

def last_row_to_json(tickers_df):
    tickers_last_info = tickers_df.swaplevel().sort_index()
    result = {
        ticker: fields.to_dict()
        for ticker, fields in tickers_last_info.groupby(level=0)
    }
    return result

def send_to_kafka():

    # Create Kafka producer
    producer = KafkaProducer(
        bootstrap_servers='192.168.1.212:9092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8'),
        key_serializer=lambda k: k.encode('utf-8'),
    )

    # Send message
    producer.send(
        topic='tickers_last_info',
        value=get_tickers_last_info(get_tickers.sp500_tickers())
    )


send_to_kafka()