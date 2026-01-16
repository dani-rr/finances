from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime
from docker.types import Mount


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
        # Run the mounted script via an absolute path inside the container
        command='python /app/lib/get_tickers.py',
        api_version='auto',
        auto_remove="force",  # updated for new provider version
        docker_url='unix://var/run/docker.sock',
        network_mode='d1_network',
        # Bind-mount host code into the task container for live development
        mounts=[
            Mount(target='/app/lib', source='/home/daniel/code/finances/lib', type='bind'),
            Mount(target='/app/src', source='/home/daniel/code/finances/src', type='bind'),
        ],
        # Ensure Python can import modules from the mounted folders
        environment={'PYTHONPATH': '/app/lib:/app/src'},
    )
