.PHONY: setup install run\ fiftyone run\ labelstudio

PYTHON_VERSION=3.13
VENV_DIR=.venv

setup:
	# Install Python 3.13 using pyenv if not already installed
	@if ! pyenv versions | grep -q $(PYTHON_VERSION); then \
		pyenv install $(PYTHON_VERSION); \
	fi
	# Create virtual environment
	pyenv local $(PYTHON_VERSION)
	@if [ ! -d "$(VENV_DIR)" ]; then \
		python -m venv $(VENV_DIR); \
	fi
	# Activate virtual environment and upgrade pip
	. $(VENV_DIR)/bin/activate; \
	pip install --upgrade pip; \
	pip install -r requirements.txt

install:
	. $(VENV_DIR)/bin/activate; \
	pip install -r requirements.txt

run fiftyone:
	. $(VENV_DIR)/bin/activate; \
	fiftyone app start

run labelstudio:
	. $(VENV_DIR)/bin/activate; \
	label-studio

