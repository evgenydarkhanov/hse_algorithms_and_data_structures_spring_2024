.DEFAULT_GOAL := start
PYTHON = python3

start:
	$(PYTHON) coins.py
	
test:
	$(PYTHON) -m unittest -v tests.py
	
clean:
	rm -rf __pycache__
