from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'spiderman',
    'retries': 5,
    'retry_delay': timedelta(minutes=1)
}

def foo(ti):
    place = "Augustiner"
    print(f"I am fooing here at {place}")
    ti.xcom_push(key="place", value = place)

def bar(ti, bar_name):
    print(f"I am here at the bar {bar_name}")
    
    new_place = ti.xcom_pull(key="place", task_ids="task_1" )
    print(f"Come here at {new_place}")

with DAG(
    dag_id = "PythonOperator-3",
    default_args = default_args,
    description = "This is the python operator",
    start_date = datetime(2023, 6, 22, 8), #year, month, day, hour
    schedule_interval = '@daily' 
) as dag:
    
    task_1 = PythonOperator(
        task_id = 'task_1',
        python_callable = foo 
    )

    task_2 = PythonOperator(
        task_id = 'task_2',
        python_callable = bar,
        op_kwargs = {
            'bar_name': "toblerone"
        } 
    )

    task_1 >> task_2
