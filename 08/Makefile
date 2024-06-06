.DEFAULT_GOAL := test

VENV = testvenv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

testvenv: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt
	
test: testvenv
	$(PYTHON) -m unittest -v tests.py
	
clean:
	rm -rf __pycache__
	rm -rf testvenv
