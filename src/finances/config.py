import os

KAFKA_BOOTSTRAP = os.getenv("KAFKA_BOOTSTRAP", "localhost:9092")
TICKERS_TOPIC = os.getenv("TICKERS_TOPIC", "sp500_tickers")
TICKERS_LAST_INFO_TOPIC = os.getenv("TICKERS_TOPIC", "tickers_last_info")