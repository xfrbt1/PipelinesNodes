requirements:
	pip install -r requirements.txt

start:
	docker-compose up --build -d

stop:
	docker-compose stop

format:
	black . && isort .
