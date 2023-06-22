from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'spiderman',
    'retries': 5,
    'retry_delay': timedelta(minutes=1)
}

with DAG(
    dag_id = "BashOperator-2",
    default_args = default_args,
    description = "This is the test dag",
    start_date = datetime(2023, 6, 22, 8), #year, month, day, hour
    schedule_interval = '@daily' 
) as dag:
    
    task_1 = BashOperator(
        task_id = 'task_1',
        bash_command = 'echo Hello World!'
    )

    task_2 = BashOperator(
        task_id = 'task_2',
        bash_command = 'echo Hello World!'
    )

    task_2 >> task_1

