.PHONY: all venv install clean

# Define the virtual environment directory
VENV_DIR = ./venv

# Define the Python interpreter to use
PYTHON = $(VENV_DIR)/bin/python

# Default target
all: venv install

# Create virtual environment if it doesn't exist
venv:
	@if [ ! -d $(VENV_DIR) ]; then \
		echo "Creating virtual environment..."; \
		python3 -m venv $(VENV_DIR); \
	fi
	@echo "Source virtualenv with:"
	@echo "source $(VENV_DIR)/bin/activate"

install: venv
	@$(PYTHON) -m pip install --upgrade pip
	@$(PYTHON) -m pip install -e .

clean:
	@echo "Removing virtual environment..."
	@rm -rf $(VENV_DIR)
