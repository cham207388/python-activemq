# Notes

## Usage

I'm using Makefile to streamline the commands. 
Commands can be found in Makefile

- start the active mq server 
  - `make active-up`
- start the postgres db container 
  - `make postgres`
- start the app to produce via an endpoint
  - `make app` or `make producer`
- start the consumer 
  - `make consumer`

## References

- [docker-image](https://hub.docker.com/r/symptoma/activemq)

## Pytest

- pip install -e
  - install missing dependencies
- 