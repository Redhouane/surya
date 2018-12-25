init:
	pip install --upgrade pip
	pip install -r requirements.txt

test:
	python -m unittest discover -s tests/unit
