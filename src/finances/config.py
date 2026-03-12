import os

KAFKA_BOOTSTRAP = os.getenv("KAFKA_BOOTSTRAP", "192.168.1.212:9092")
TICKERS_TOPIC = os.getenv("TICKERS_TOPIC", "sp500_tickers")
TICKERS_LAST_INFO_TOPIC = os.getenv("TICKERS_LAST_INFO_TOPIC", "tickers_last_info")