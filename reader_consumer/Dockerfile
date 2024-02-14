FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /reader_consumer

COPY pyproject.toml .

RUN pip install poetry

RUN poetry install

COPY . .

ENV PYTHONPATH=$PYTHONPATH:/