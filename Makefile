all: build up

build:
	docker-compose build
	@echo  === Docker containers sucessfully built ===

start: up

run: up

up:
	docker-compose up
	@echo  === Docker containers up and running ===

stop: down

down:
	docker-compose down
	@echo  === Docker containers stopped and deleted ===
