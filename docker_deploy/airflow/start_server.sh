#!/bin/bash

# # Start the first process
cd dir_mlflow
./mlflow server --host 0.0.0.0 --port 5000 &
cd /mlops_tools/dir_airflow

airflow db migrate 

airflow users create \
--username root \
--password root \
--firstname Peter \
--lastname Parker \
--role Admin \
--email spiderman@superhero.org


# Start the second process
# cd ../dir_airflow 
airflow webserver --port 8000 &

# Start the third process
airflow scheduler &

# Wait for any process to exit
wait -n

# Exit with status of process that exited first
exit $?