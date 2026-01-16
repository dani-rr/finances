from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime
from docker.types import Mount

with DAG(
    dag_id='quarter_hour_get_tickers_info',
    start_date=datetime(2024, 1, 1),
    schedule='*/15 * * * *',  # every 15 minutes
    catchup=False
):
    DockerOperator(
        task_id='get_tickers_last_info',
        image='finances:latest',
        # Run the mounted script via an absolute path inside the container
        command='python /app/lib/get_tickers_last_info.py',
        api_version='auto',
        auto_remove="force",  # updated for new provider version
        docker_url='unix://var/run/docker.sock',
        # Place the task container on the same Docker network as Kafka
        network_mode='d1_network',
        # Bind-mount host code into the task container for live development
        mounts=[
            Mount(target='/app/lib', source='/home/daniel/code/finances/lib', type='bind'),
            Mount(target='/app/src', source='/home/daniel/code/finances/src', type='bind'),
        ],
        # Ensure Python can import modules from the mounted folders
        environment={'PYTHONPATH': '/app/lib:/app/src'},
    )
