import os
from dotenv import load_dotenv
load_dotenv("infra/postgres/.env")

KAFKA_BOOTSTRAP = os.getenv("KAFKA_BOOTSTRAP", "192.168.1.212:9092")
TICKERS_TOPIC = os.getenv("TICKERS_TOPIC", "sp500_tickers")
TICKERS_LAST_INFO_TOPIC = os.getenv("TICKERS_LAST_INFO_TOPIC", "tickers_last_info")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")
POSTGRES_DB = os.getenv("POSTGRES_DB", "finances")
POSTGRES_USER = os.getenv("POSTGRES_USER", "finances")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")