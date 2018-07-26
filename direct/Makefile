all: build down up

build:
	docker-compose build
	@echo  === Docker containers sucessfully built ===

start: build down up

run: down up

up: down build
	docker-compose up
	@echo  === Docker containers up and running ===

stop: down

down:
	docker-compose down
	@echo  === Docker containers stopped and deleted ===
