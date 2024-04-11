PYTHON = python3

start:
	$(PYTHON) solution.py
	
generate:
	$(PYTHON) generate_data.py

test:
	$(PYTHON) -m unittest -v tests.py

clean:
	rm -rf __pycache__
	cd ./test_data && rm *.txt

