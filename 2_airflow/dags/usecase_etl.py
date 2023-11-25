import pandas as pd
import numpy as np
from datetime import date
from airflow.decorators import task

@task
def perform_etl(filepath):

    df = pd.read_csv(filepath)
    cols_to_remove = df.corr().index[abs(df.corr()['quality']) < 0.1].tolist()
    df.drop(columns = cols_to_remove, inplace=True)
    
    filename = filepath.split('.')[0] + '_' + str(date.today()) + '.csv'
    df.to_csv(filename,index=False)

    return filename

# perform_etl("data/winequality-red.csv")