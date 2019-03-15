init:
	pip install --upgrade pip
	pip install -r requirements.txt

run-sp:
	docker run -d -p 8080:8080 --rm allenai/scienceparse:2.0.3

stop-sp:
	docker stop elastic_davinci

test:
	python -m unittest discover -s tests/unit
