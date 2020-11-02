test:
	python3 -m unittest tests/http_test.py
	python3 -m unittest tests/validator_test.py
	python3 -m unittest tests/date_test.py
	python3 -m unittest tests/week_test.py