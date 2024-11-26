# Proměnné
DOCKER_COMPOSE = docker compose
SERVICE = web

# Build a spuštění
build:
	$(DOCKER_COMPOSE) build

up:
	$(DOCKER_COMPOSE) up -d

down:
	$(DOCKER_COMPOSE) down

logs:
	$(DOCKER_COMPOSE) logs -f $(SERVICE)

# Django příkazy
web:
	$(DOCKER_COMPOSE) exec $(SERVICE) python3 manage.py $(filter-out $@,$(MAKECMDGOALS))

# Alias pro nejčastější příkazy
#migrate: web migrate
#makemigrations: web makemigrations
createsuperuser: web createsuperuser
shell: web shell

# Defaultní pravidlo pro neznámé cíle
%:
	@:
