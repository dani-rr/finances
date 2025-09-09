from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime

with DAG(
    dag_id='daily_get_tickers',
    start_date=datetime(2024, 1, 1),
    schedule='@daily',
    catchup=False,
    tags=["kafka", "tickers"]
):
    DockerOperator(
        task_id='get_tickers',
        image='finances:latest',
        command='python lib/get_tickers.py',
        api_version='auto',
        auto_remove="force",  # updated for new provider version
        docker_url='unix://var/run/docker.sock',
        network_mode='d1_network'
    )