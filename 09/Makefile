.DEFAULT_GOAL := start
PYTHON = python3

start:
	$(PYTHON) rectangle.py
	
test:
	$(PYTHON) -m unittest -v tests.py
	
clean:
	rm -rf __pycache__
