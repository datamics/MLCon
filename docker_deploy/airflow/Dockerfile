FROM python:3.8

ENV AIRFLOW_VERSION=2.7.3

# create airflow directory
RUN mkdir "mlops_tools" "mlops_tools/dir_airflow" "mlops_tools/data" &&\
    cd "mlops_tools/dir_airflow" &&\
    mkdir dags logs plugins 

ENV AIRFLOW_HOME=/mlops_tools/dir_airflow

WORKDIR "/mlops_tools/dir_airflow"

## install airflow
RUN pip3 install --upgrade pip &&\
    PYTHON_VERSION="$(python --version | cut -d " " -f 2 | cut -d "." -f 1-2)" &&\
    CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt" &&\
    pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"

# Install essential packages
RUN pip3 install pandas numpy scikit-learn boto3 matplotlib mlflow

# # initialise airflow DB 
COPY start_server.sh /mlops_tools/start_server.sh

COPY winequality-red.csv /mlops_tools/data/winequality.csv
