install:
	poetry install
	poetry add prompt

start:
	poetry run brain-games

lint:
	potery run flake8 brain_games