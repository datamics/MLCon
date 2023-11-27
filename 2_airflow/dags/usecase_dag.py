from airflow.decorators import task, dag
from airflow.operators.bash import BashOperator
import usecase_etl, usecase_trainining
from datetime import datetime, timedelta
import os

import mlflow

default_args = {
    'owner': 'MLCon_berlin',
    'retries': 5,
    'retry_delay' : timedelta(minutes=1)
}

experiment_name = "From DAG"

@dag(
    dag_id="Usecase",
    default_args=default_args,
    description="this is our first DAG",
    start_date=datetime(2023, 11, 26, 8),     # year, month, date, time
    schedule_interval="@daily"
)
def dag_function(filepath):

    filename = usecase_etl.perform_etl(filepath)
    mlflow.set_tracking_uri("http://127.0.0.1:5000")
    mlflow.set_experiment(experiment_name)
    run_id = usecase_trainining.perform_training(filename, experiment_name)

    command = f"""
            cd {path_root};
            git add .;
            git commit -m "Training with MLFlow run_id {run_id}";
            git push
            """

    git_commit = BashOperator(
        task_id = "task_3",
        bash_command= command
    )


    filename >> run_id >> git_commit

path_root = os.getcwd()
os.chdir("../")
path_data = os.path.join(os.getcwd(), "data", "winequality.csv")

taskflow_dag = dag_function(path_data)
