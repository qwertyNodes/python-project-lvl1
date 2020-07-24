install:
	poetry install
start:
	poetry run brain-games

lint:
	poetry run flake8 brain_games