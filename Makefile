test:
	coverage run --source=. -m pytest tests/*_test.py
	coverage report
	coverage html
	coveralls

cov:
	coverage report
	coverage html

lint:
	flake8 --statistics --count

update:
	git pull
	pip3 install -r requirements.txt	
