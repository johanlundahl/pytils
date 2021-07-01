test:
	python3 -m pytest tests/*_test.py

lint:
	flake8 --statistics --count
