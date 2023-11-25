from datetime import datetime, timedelta
from airflow.decorators import dag, task
from usecase_etl import perform_etl
from usecase_training import training
from airflow.operators.bash import BashOperator
import logging
import mlflow
import os

default_args = {
    'owner': 'John',
    'retries': 5,
    'retry_delay': timedelta(minutes=1),
    'tracking_url':'http://127.0.0.1:5000',
    'exp_name': 'from DAGS'
}

@dag(dag_id='dag_with_usecase', 
    default_args=default_args, 
    start_date=datetime(2023, 11, 22, 5), 
    schedule_interval='@daily')
def dag_func(datapath):    
    
    # set tracking and db registry
    mlflow.set_tracking_uri(default_args['tracking_url'])

    # Use default location and set a new experiment name
    mlflow.set_experiment(default_args['exp_name'])

    filename = perform_etl(datapath)
    run_id = training(filename, default_args['exp_name'])

    git_command = f"""
                    cd '{path_root}';
                    git add .;
                    git commit -m "Training with MLFlow run_id {run_id}";
                    git push;
                """

    git_commit = BashOperator(
        task_id = 'git_commit',              
        bash_command = git_command
        )

    filename >> run_id >> git_commit

# get paths
path_root = os.getcwd()
logging.info(f"current directory {os.getcwd()}")

# change to absolute path of data folder
os.chdir("../")
path_data = os.path.join(os.getcwd(), "data", "winequality.csv")

# datapath = "/Volumes/Macintosh HD - Daten/Work/Univ/TUM/Datamics/MLCon/MLCon Munich/Workshop/Code/data/winequality.csv"
taskflow_dag = dag_func(path_data)