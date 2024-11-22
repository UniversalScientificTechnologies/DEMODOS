#!/bin/bash

# Spuštění Python skriptu v tmux relaci
tmux new-session -d -s generator "python3 /app/generate_html.py"

# Spuštění Nginx v popředí
nginx -g "daemon off;"
