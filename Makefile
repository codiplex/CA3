install:
	pip install -r requirements.txt

test:
	python -m pytest -vv --cov=task test_task.py