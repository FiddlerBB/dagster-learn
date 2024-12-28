# Makefile for Dagster development

# Set DAGSTER_HOME environment variable
export DAGSTER_HOME := $(shell pwd)

STORAGE_DIR=$(DAGSTER_HOME)/storage

.PHONY: init run

init:
	@if [ ! -d "$(STORAGE_DIR)" ]; then \
		mkdir -p "$(STORAGE_DIR)" && \
		chmod 755 "$(STORAGE_DIR)" && \
		echo "Directory created: $(STORAGE_DIR)"; \
	else \
		echo "Directory already exists: $(STORAGE_DIR)"; \
	fi

	python3 setup.py
run:
	@echo "Setting DAGSTER_HOME to: $(DAGSTER_HOME)"
	dagster dev

.DEFAULT_GOAL := run
