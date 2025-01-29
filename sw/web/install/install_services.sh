#!/bin/bash

# Cesta k vašim systemd souborům
SYSTEMD_FILES_PATH="../systemd/"
TARGET_PATH="/etc/systemd/system/"

echo "Instaluji systemd služby pro DEMODOs..."

# Kontrola, jestli existuje složka se službami
if [ ! -d "$SYSTEMD_FILES_PATH" ]; then
  echo "Chyba: Složka $SYSTEMD_FILES_PATH neexistuje!" >&2
  exit 1
fi

# Kopírování služeb
echo "Kopíruji systemd služby do $TARGET_PATH..."
for service_file in "$SYSTEMD_FILES_PATH"*.service; do
  if [ -f "$service_file" ]; then
    cp "$service_file" "$TARGET_PATH"
    echo "Kopírován: $(basename "$service_file")"
  fi
done

# Načtení nových služeb
echo "Načítám nové systemd služby..."
systemctl daemon-reload

# Povolení a spuštění služeb
echo "Povoluji a spouštím služby..."
for service_file in "$SYSTEMD_FILES_PATH"*.service; do
  service_name=$(basename "$service_file")
  echo "Povoluji $service_name..."
  systemctl enable "$service_name"
  echo "Spouštím $service_name..."
  systemctl start "$service_name"
done

echo "Instalace systemd služeb dokončena!"
