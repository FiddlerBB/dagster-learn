# Makefile for Dagster development

# Set DAGSTER_HOME environment variable
# export DAGSTER_HOME := $(shell pwd)
export DAGSTER_HOME := $(abspath $(shell pwd))

STORAGE_DIR := $(DAGSTER_HOME)/storage
# STORAGE_DIR=$(shell dirname $(data))
export SQLITE_STORAGE_BASE_DIR := $(STORAGE_DIR)
export LOCAL_ARTIFACT_STORAGE := $(STORAGE_DIR)/artifacts
export COMPUTE_LOGS := $(STORAGE_DIR)/compute_logs
export HISTORY_STORAGE := $(STORAGE_DIR)/history
export SCHEDULES_STORAGE := $(STORAGE_DIR)/schedules

.PHONY: init run

init:
	@if [ ! -d "$(STORAGE_DIR)" ]; then \
		mkdir -p "$(STORAGE_DIR)" && \
		chmod 755 "$(STORAGE_DIR)" && \
		echo "Directory created: $(STORAGE_DIR)"; \
	else \
		echo "Directory already exists: $(STORAGE_DIR)"; \
	fi

	pip install -e ".[dev]"
run:
	@echo "Setting DAGSTER_HOME to: $(DAGSTER_HOME)"
	dagster dev

.DEFAULT_GOAL := run
