build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down

pip-install-venv:
	pip install -r requirements.txt
	pip install -r requirements.dev.txt

lint-flake8:
	docker-compose run --rm app sh -c "flake8"

lint-black:
	docker-compose run --rm app sh -c "black --check ."

lint-isort:
	docker-compose run --rm app sh -c "isort --check ."

lint:	lint-isort lint-black lint-flake8
