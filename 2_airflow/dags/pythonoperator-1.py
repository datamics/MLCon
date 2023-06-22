from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'spiderman',
    'retries': 5,
    'retry_delay': timedelta(minutes=1)
}

def foo():
    print("I am fooing here..")

with DAG(
    dag_id = "PythonOperator-1",
    default_args = default_args,
    description = "This is the python operator",
    start_date = datetime(2023, 6, 22, 8), #year, month, day, hour
    schedule_interval = '@daily' 
) as dag:
    
    task_1 = PythonOperator(
        task_id = 'task_1',
        python_callable = foo 
    )
