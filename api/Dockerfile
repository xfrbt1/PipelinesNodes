FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /api

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

ENV PYTHONPATH=$PYTHONPATH:/
