FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /parser_producer

COPY pyproject.toml .

RUN pip install poetry

RUN poetry install

COPY . .

ENV PYTHONPATH=$PYTHONPATH:/




#FROM python:3.10-slim
#
#ENV PYTHONUNBUFFERED=1
#ENV PYTHONDONTWRITEBYTECODE=1
#
#WORKDIR /parser_producer
#
#RUN apt-get update \
#    && apt-get install -y --no-install-recommends \
#        libpq-dev \
#    && rm -rf /var/lib/apt/lists/*
#
#RUN pip install poetry
#
#COPY pyproject.toml .
#
#RUN poetry install --no-root
#
#COPY . .
#
#WORKDIR /parser_producer
#
#CMD ["poetry", "run", "celery", "-A", "your_module_name", "worker", "--loglevel=INFO"]


