FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

USER root

RUN groupadd -g 110 docker && usermod -aG docker root

USER root 

CMD ["python", "lib/get_tickers.py"]
