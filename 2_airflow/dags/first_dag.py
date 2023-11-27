from airflow import DAG
from airflow.operators.bash import BashOperator

from datetime import datetime, timedelta

default_args = {
    'owner': 'MLCon_berlin',
    'retries': 5,
    'retry_delay' : timedelta(minutes=1)
}

with DAG(
    dag_id="first_dag",
    default_args=default_args,
    description="this is our first DAG",
    start_date=datetime(2023, 11, 26, 8),     # year, month, date, time
    schedule_interval="@daily"
    ) as dag:
    

    task_1 = BashOperator(
        task_id = "task_1",
        bash_command= "echo Hello World!"
    )

    task_1