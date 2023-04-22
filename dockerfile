FROM python:3.6-alpine

ARG AWS_ACCESS_KEY_ID=access_key
ARG AWS_SECRET_ACCESS_KEY=secret_key
ARG AWS_REGION=us-east-2

# install dependencies
RUN pip install --upgrade pip
COPY ./cicd.py .
RUN pip install boto3
RUN python cicd.py
