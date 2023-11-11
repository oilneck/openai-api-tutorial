FROM python:3.9.7-buster

RUN apt-get update && \
    apt-get install -y libgl1-mesa-glx && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /contents/src
RUN pip install --upgrade pip
RUN pip install openai
RUN pip install ipython

# env
ARG OPENAI_API_KEY
ENV OPENAI_API_KEY=${OPENAI_API_KEY}
ENV PYTHONPATH=/contents/src