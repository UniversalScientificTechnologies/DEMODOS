#!/bin/bash

# Načtení proměnných z .env
source .env

echo "Vytvářím Django .env soubor..."
sudo mkdir /opt/demodos ||true
cat <<EOF > /opt/demodos/.env
DJANGO_SECRET_KEY=$DJANGO_SECRET_KEY
DB_NAME=$DB_NAME
DB_USER=$DB_USER
DB_PASSWORD=$DB_PASSWORD
DB_HOST=$DB_HOST
DB_PORT=$DB_PORT
REDIS_HOST=$REDIS_HOST
REDIS_PORT=$REDIS_PORT
DJANGO_DEBUG=$DJANGO_DEBUG
EOF
