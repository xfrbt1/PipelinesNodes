FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /web_src

COPY pyproject.toml .

RUN pip install poetry

RUN poetry install

COPY . .

ENV PYTHONPATH=$PYTHONPATH:/