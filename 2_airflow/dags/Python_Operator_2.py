from airflow import DAG
from airflow.operators.python import PythonOperator

from datetime import datetime, timedelta

default_args = {
    'owner': 'MLCon_berlin',
    'retries': 5,
    'retry_delay' : timedelta(minutes=1)
}

def foo(ti, args):
    args = args
    # ti = kwargs['ti']
    print(f"I am Foo-ing here! at {args}")
    ti.xcom_push( key = 'place', value = args)

def bar(ti):
    # ti = kwargs['ti']
    place_name = ti.xcom_pull( key = 'place', task_ids = 'py_task_2')
    print(f"I want to come to {place_name}")

    

with DAG(
    dag_id="Python_Operator_2",
    default_args=default_args,
    description="this is our first DAG",
    start_date=datetime(2023, 11, 26, 8),     # year, month, date, time
    schedule_interval="@daily"
    ) as dag:
    
    task_1 = PythonOperator(
        task_id = 'py_task_2',
        python_callable= foo,
        op_kwargs={
            'place': 'MLCon Berlin'
        },
        provide_context=True
    )

    task_2 = PythonOperator(
        task_id = 'py_task_3',
        python_callable= bar,
        provide_context=True
    )

    task_1 >> task_2

    