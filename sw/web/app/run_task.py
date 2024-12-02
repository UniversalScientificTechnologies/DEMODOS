# run_task.py

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demodos_ui.settings')
django.setup()  # Inicializace musí být před importem modelů

from tasks import background_task

if __name__ == "__main__":
    print("Starting background task...")
    background_task()