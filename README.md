# Boilerplate UI Testing

The purpose of this project is to create a boilerplate entrypoint into doing UI-based
testing. This will eventually support both Selenium and Cypress, but currently only supports
Selenium-based testing using pytest.

## Current supported browsers

- Firefox

## Makefile as Interface

Below are the exiting makefile targets:

- python-docker
- python-headless-test
- python-test

### python-docker

The python-docker makefile target will build a docker container used for running tests. Right now this
is mostly only useful for the dependency chain of the makefile.

### python-headless-tst

This will use docker to spin up a headless web environment.

### python-test

This makefile target is a helper for quickly executing selenium-based python tests localy instead of
embedded in a docker container.

NOTE: This requires you have Firefox installed, and have the gecko driver in the executable path.