clean:
	pre-commit run --all-files
build:
	docker compose -f local.yml up --build -d --remove-orphans
build-log:
	docker compose -f local.yml up --build

up:
	docker compose -f local.yml up -d

down:
	docker compose -f local.yml down

show-logs:
	docker compose -f local.yml logs

show-logs-api:
	docker compose -f local.yml logs server

collectstatic:
	docker compose -f local.yml run --rm server python manage.py collectstatic --no-input --clear

createsuperuser:
	cd backend & python manage.py createsuperuser

makemigrations:
	cd backend & python manage.py makemigrations

migrate:
	cd backend & python manage.py migrate

makemigrations-docker:
	docker compose -f local.yml run --rm server python manage.py makemigrations

migrate-docker:
	docker compose -f local.yml run --rm server python manage.py migrate

down-v:
	docker compose -f local.yml down -v
cov:
	cd backend & coverage run --source='.' --omit='*/migrations/*.py,*/asgi.py,*/wsgi.py,*/manage.py' manage.py test
cov-gen:
	cd backend & coverage html

cov-docker:
	docker compose -f local.yml run --rm server coverage run --source='.' --omit='*/migrations/*.py,*/asgi.py,*/wsgi.py,*/manage.py' manage.py test

cov-gen-docker:
	docker compose -f local.yml run --rm server coverage html
