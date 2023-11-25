FROM python:3.10

RUN pip3 install mlflow

RUN mkdir mlops_tools  &&\
    mkdir "mlops_tools/dir_mlflow" &&\
    mkdir "mlops_tools/dir_mlflow/artifact_store"

WORKDIR "mlops_tools/dir_mlflow"

EXPOSE 5000



### Commands!!
# CMD mlflow server \
#     --host 0.0.0.0 \
#     --port 5000

### Build docker image
# docker build -t mlflow:v1 . 

### Run container
# docker run -v <local path to mount>:/mlflow_dir -p 5050:5000  mlflow:v1