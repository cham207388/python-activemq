active-up:
	docker-compose up -d

active-down:
	docker-compose down -v

app:
	uvicorn main:app --reload

producer:
	uvicorn main:app --reload

consumer:
	python consumer_fanout.py

postgres:
	docker container run --name load:123 --rm -e POSTGRES_DB=activemq -e POSTGRES_USER=baicham -e POSTGRES_PASSWORD=password -p 5433:5432 -d postgres

stop-pg:
	docker container stop postgres_active

freeze:
	pip freeze > requirements.txt


in-one:
