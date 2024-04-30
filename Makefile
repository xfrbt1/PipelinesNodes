start:
	docker-compose up --build -d

stop:
	docker-compose stop

format:
	black . && isort .
