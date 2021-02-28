.PHONY: hello run venv install
SHELL := /bin/bash

hello:
	echo "hello world"

lint:
	pre-commit run --all-files

install:
	source venv/bin/activate \
	pip install .

test:
	source venv/bin/activate \
	pip install . \
	pytest -vv tests/

run:
	venv/bin/pserve development.ini
