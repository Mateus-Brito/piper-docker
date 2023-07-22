download:
	docker-compose -f ./services/download/docker-compose.yml build download && docker-compose -f ./services/download/docker-compose.yml run --rm download bash

start:
	docker-compose up

stop:
	docker-compose down

install:
	@make download
	@make start
