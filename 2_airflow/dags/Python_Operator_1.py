from airflow import DAG
from airflow.operators.python import PythonOperator

from datetime import datetime, timedelta

default_args = {
    'owner': 'MLCon_berlin',
    'retries': 5,
    'retry_delay' : timedelta(minutes=1)
}

def foo():
    print("I am Foo-ing here!")

with DAG(
    dag_id="Python_Operator_1",
    default_args=default_args,
    description="this is our first DAG",
    start_date=datetime(2023, 11, 26, 8),     # year, month, date, time
    schedule_interval="@daily"
    ) as dag:
    
    task_1 = PythonOperator(
        task_id = 'py_task_1',
        python_callable= foo
    )

    task_1

    