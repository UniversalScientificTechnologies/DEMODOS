#!/bin/bash

echo "Instaluji závislosti: PostgreSQL, Redis, Python..."
apt update && apt install -y postgresql redis python3 python3-pip python3-venv libpq-dev
