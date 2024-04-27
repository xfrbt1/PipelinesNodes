start:
	docker-compose up --build -d

format:
	black . && isort .
