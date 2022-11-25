test:
	#python3 -m pytest tests/*_test.py
	coverage run -m pytest tests/*_test.py

cov:
	coverage report
	coverage html

lint:
	flake8 --statistics --count

update:
	git pull
	pip3 install -r requirements.txt	
