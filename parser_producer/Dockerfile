FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /parser_producer

COPY pyproject.toml .

RUN pip install poetry

RUN poetry install

COPY . .

ENV PYTHONPATH=$PYTHONPATH:/

CMD ["poetry", "run", "python", "-m", "run"]



