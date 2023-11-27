import pandas as pd 
from datetime import date

from airflow.decorators import task

@task
def perform_etl(filepath):

    df = pd.read_csv(filepath)
    cols_to_remove = df.corr().index[abs(df.corr()['quality']) < 0.1].tolist()
    df2 = df.drop(cols_to_remove, axis = 1)

    filename = filepath.split('.')[0] + '_' + str(date.today()) + ".csv"
    df2.to_csv(filename, index=False)

    return filename

