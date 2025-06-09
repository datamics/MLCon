.PHONY: setup install run\ fiftyone run\ labelstudio

PYTHON_VERSION=3.12
VENV_DIR=.venv

setup:
	@if ! command -v python$(PYTHON_VERSION) >/dev/null 2>&1; then \
		echo "Python $(PYTHON_VERSION) is not installed locally."; \
		if [ "$(shell uname)" = "Darwin" ]; then \
			brew install python@$(PYTHON_VERSION); \
		else \
			echo "Please install Python $(PYTHON_VERSION) manually."; \
			exit 1; \
		fi; \
	fi
	@if [ ! -d "$(VENV_DIR)" ]; then \
		python$(PYTHON_VERSION) -m venv $(VENV_DIR); \
	fi
	. $(VENV_DIR)/bin/activate; \
	pip install --upgrade pip; \
	pip install -r requirements.txt

install:
	. $(VENV_DIR)/bin/activate; \
	pip install -r requirements.txt

run\ fiftyone:
	. $(VENV_DIR)/bin/activate; \
	fiftyone app start

run\ labelstudio:
	. $(VENV_DIR)/bin/activate; \
	label-studio

check:
	@if ! command -v python3.12 >/dev/null 2>&1; then \
		echo "Python 3.12 is not installed locally."; \
		exit 1; \
	else \
		echo "Python  $(PYTHON_VERSION) is already installed in the machine."; \
	fi

