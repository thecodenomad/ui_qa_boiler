#####################################################################
# Copyright (c) codenomad (codenomad@gmail.com) All rights reserved #
#####################################################################

TOPDIR := ${CURDIR}

.PHONY: python-docker
python-docker:
	docker build -f docker/Dockerfile.python . --tag docked-python:latest

.PHONY: python-headless-test
python-headless-test: python-docker
	docker run -v $(PWD)/screenshots:/code/screenshots --env HEADLESS=true docked-python:latest

.PHONY: python-test
python-test:
	pytest -s src/python/test*.py -m "not flakey"

python-test-all:
	pytest -s src/python/test*.py