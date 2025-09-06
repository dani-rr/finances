from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime

with DAG(
    dag_id='quarter_hour_get_tickers_info',
    start_date=datetime(2024, 1, 1),
    schedule='*/15 * * * *',  # every 15 minutes
    catchup=False
):
    DockerOperator(
        task_id='get_tickers_last_info',
        image='finances:latest',
        command='python lib/get_tickers_last_info.py',
        api_version='auto',
        auto_remove="force",  # updated for new provider version
        docker_url='unix://var/run/docker.sock',
        network_mode='bridge'
    )
