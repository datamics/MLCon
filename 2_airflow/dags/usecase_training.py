import pandas as pd
import numpy as np

from sklearn.linear_model import ElasticNet
from sklearn.model_selection import train_test_split
from sklearn import metrics
import matplotlib.pyplot as plt
import logging
import mlflow

from airflow.decorators import task

def eval_metrics(ground_truth, pred):
    
    rmse = np.sqrt(metrics.mean_squared_error(ground_truth, pred))
    mae = metrics.mean_absolute_error(ground_truth, pred)
    r2 = metrics.r2_score(ground_truth, pred)
    
    return rmse, mae, r2

@task
def training(data_path, experiment_name):

    import mlflow

    mlflow.autolog()

    # Read the wine-quality csv file
    df = pd.read_csv(data_path)
    np.random.seed(40)

    # Split the data into training and test sets. (0.75, 0.25) split.
    X = df.drop('quality',axis=1)
    y = df['quality']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=43)

    ### Train the model ###

    #######################################################
    ################### MLflow code #######################
    #######################################################

    ## set artifact
    # Not required already set in the server 

    ## add db_path - already set in the DAG file, task cannot access directly
    # db_path = "/Users/saumyagoyal/JupyterNotebook/mlcon_mlflow/backend_store/new_backend_store.db"
    # db_uri = "sqlite:///" + db_path

    ## set tracking and db registry - already set in the DAG file, task cannot access directly
    # mlflow.set_registry_uri(db_uri)
    # mlflow.set_tracking_uri("0.0.0.0:5000")

    ## adding tags for each run
    tags = {"Demo": "True", "created-by": "John"}

    ## set experiment name
    # already set in the DAG file


    ## set curent run name
    current_run_name = "Logging with airflow task"
    
    ## Set a new experiment name 
    # Not required already set in the DAG function 

    with mlflow.start_run(run_name=current_run_name) as run:
        
        alpha = 0.1
        l1 = 0.5
        
        logging.info("1")
        lr = ElasticNet(alpha=alpha, l1_ratio=l1)
        lr.fit(X_train,y_train)

        # Get prediction on Test dataset
        y_pred = lr.predict(X_train)

        # Check model performance on test
        (rmse, mae, r2) = eval_metrics(y_train,y_pred)
        print(f"Dataset: Training \nRMSE:{rmse}\nMAE: {mae}\nR2:{r2}")

        ###################### Logging code ######################
        
        #log parameters of the model
        mlflow.log_param("alpha", alpha)
        mlflow.log_param("l1_ratio", l1)
        
        # log metrics 
        mlflow.log_metric("rmse", rmse)
        mlflow.log_metric("r2", r2)
        mlflow.log_metric("mae", mae)
        
        # log tags
        mlflow.set_tags(tags)

        ########### logging the model in artifact store ###################
        mlflow.sklearn.log_model(lr, "Linear regression model")
        
        # check the storage locations
        print(f"\nTracking URI {mlflow.get_tracking_uri()}")
        print(f"Artifact location {mlflow.get_artifact_uri()}")
        ##############################################################
        return run.info.run_id