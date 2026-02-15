.PHONY: run install clean

run:
	python3 main.py

install:
	pip install -r requirements.txt

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -rf *.pyc
