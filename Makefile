.PHONY: help

help: ## Show this help message with aligned shortcuts, descriptions, and commands
	@awk 'BEGIN {FS = ":"; printf "\033[1m%-20s %-40s %s\033[0m\n", "Target", "Description", "Command"} \
	/^[a-zA-Z_-]+:/ { \
		target=$$1; \
		desc=""; cmd="(no command)"; \
		if ($$2 ~ /##/) { sub(/^.*## /, "", $$2); desc=$$2; } \
		getline; \
		if ($$0 ~ /^(\t|@)/) { cmd=$$0; sub(/^(\t|@)/, "", cmd); } \
		printf "%-20s %-40s %s\n", target, desc, cmd; \
	}' $(MAKEFILE_LIST)

start-activemq: # start activemq
	docker-compose up -d

stop-activemq: # Stop activemq
	docker-compose down -v

app: # Start producer
	uvicorn main_producer:app --reload

producer:
	uvicorn main_producer:app --reload

consumers: # start consumers
	python main_consumers.py

start-postgres: # start postgres container
	docker container run --rm --name postgres_active -e POSTGRES_DB=activemq -e POSTGRES_USER=baicham -e POSTGRES_PASSWORD=password -p 5433:5432 -d postgres

stop-postgres: # stop postgres container
	docker container stop postgres_active

freeze: # freeze dependencies into requirements.txt
	pip freeze > requirements.txt

venv: # start virtual environment
	python3 -m venv .venv

source: # source virtual environment
	source .venv/bin/activate