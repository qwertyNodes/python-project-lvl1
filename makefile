install:
	poetry install
start:
	poetry run brain-games

lint:
	potery run flake8 brain-games