FROM python:3.12-slim

WORKDIR /app

# Install system deps for pandas/lxml
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libxml2-dev \
    libxslt1-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your code
COPY . .

CMD ["python", "lib/get_tickers.py"]

