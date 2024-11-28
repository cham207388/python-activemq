# P2 Project

This project about ActiveMQ using Python. There are two consumers and two producers. The simple endpoints is used to
produce messages to the first queue. Which is then consumed, produced, and stored in a database before producing to
the second queue.
---

## Python Version

This project was built using **Python 3.11**

---

## Modules

* mkdocs >= 1.6.1
* numpy >= 2.1.3
* pandas >= 2.2.3
* psycopg2-binary >= 1.5.2
* stomp.py >= 0.13.2
* sqlmodel >= 1.40.1
* setuptools==75.6.0
* PyMySQL==1.1.1
* cryptography==43.0.3
* python-dotenv==1.0.1
* uvicorn==0.32.0
* fastapi==0.115.5
* mkdocs==1.6.1
* mkdocstrings-python

---

## Quick Setup

Use Makefile for commands

- start the active mq broker
- start the postgres container
- start the producer
- start the consumers

