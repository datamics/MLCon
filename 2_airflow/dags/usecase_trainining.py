import pandas as pd
import numpy as np

from sklearn.linear_model import ElasticNet
from sklearn.model_selection import train_test_split
from sklearn import metrics

import mlflow

from airflow.decorators import task

mlflow.sklearn.autolog(log_models = True)

@task
def perform_training(file_path, experiment_name):

    def eval_metrics(ground_truth, pred):
        
        rmse = np.sqrt(metrics.mean_squared_error(ground_truth, pred))
        mae = metrics.mean_absolute_error(ground_truth, pred)
        r2  = metrics.r2_score(ground_truth, pred)
        
        return rmse, mae, r2

    df = pd.read_csv(file_path)

    X = df.drop('quality', axis = 1)
    y = df['quality']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=43)

    ################# mlflow logging code

    # experiment_name = "Exp-3"
    run_name = "running from DAG"
    # artifact_store_location = "/Users/saumyagoyal/JupyterNotebook/MLCon/MLCon_23W/MLCon/artifact_store"

    tags = {
        "Demo": "True",
        "Created by": "Saumya"
    }

    # mlflow.create_experiment(experiment_name, artifact_store_location)
    mlflow.set_experiment(experiment_name)


    with mlflow.start_run(run_name=run_name) as run:
        

        alpha = 0.2
        l1 = 0.5

        lr = ElasticNet(alpha=alpha, l1_ratio=l1)
        lr.fit(X_train, y_train)

        y_pred = lr.predict(X_train)
        rmse, mae, r2 = eval_metrics(y_train, y_pred)
        
        # actual logging parameters and metrics
        
    #     # logged hyperparamters
    #     mlflow.log_param("alpha", alpha)
    #     mlflow.log_param("l1 ratio", l1)
        
    #     # logged metrics
    #     mlflow.log_metric("rmse", rmse)
    #     mlflow.log_metric("mae", mae)
    #     mlflow.log_metric("r2", r2)
        
        ## log tags
        mlflow.set_tags(tags)
        
    #     mlflow.sklearn.autolog(log_models = True)
        
        return run.info.run_id