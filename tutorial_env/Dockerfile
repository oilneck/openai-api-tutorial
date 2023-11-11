FROM python:3.9.7-buster

RUN apt-get update && \
    apt-get install -y libgl1-mesa-glx && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /contents
RUN pip install --upgrade pip
COPY ./tutorial_env/requirements.txt /contents/requirements.txt
RUN pip install -r requirements.txt
WORKDIR /contents/src

# env
ARG OPENAI_API_KEY
ENV OPENAI_API_KEY=${OPENAI_API_KEY}
ENV PYTHONPATH=/contents/src