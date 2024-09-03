FROM nginx:latest

RUN apt-get update && apt-get install -y python3 python3-pip tmux

WORKDIR /app

# Kopírování Python skriptu a requirements.txt do pracovního adresáře
COPY generate_html.py /app/generate_html.py
COPY requirements.txt /app/requirements.txt

# Instalace Python závislostí
#RUN apt-get update && apt-get install -y python3-ncurses
#RUN pip3 install -r /app/requirements.txt --break-system-packages

# Kopírování Nginx konfigurace
COPY nginx.conf /etc/nginx/nginx.conf


# Kopírování start.sh skriptu do kontejneru
COPY start.sh /app/start.sh

# Nastavení spustitelného příznaku pro start.sh
RUN chmod +x /app/start.sh

# Expozice portu 80 pro Nginx
EXPOSE 80

# Spuštění Nginx jako hlavního procesu
#CMD ["nginx", "-g", "daemon off;"]
CMD ["/app/start.sh"]
