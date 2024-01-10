#!/usr/bin/env bash
# A Bash script that sets up your web servers for the deployment of web_static

if command -v nginx &> /dev/null;then
        # Do nothing if Nginx is already installed
        true
else
        sudo apt-get update
        sudo apt-get -y install nginx
fi

sudo ufw allow 'Nginx HTTP'

# Create the deployment directory
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

# Create the index.html in the directory
sudo touch /data/web_static/releases/test/index.html

# Creating the required symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Changing owner recursively to /data directory
sudo chown -R ubuntu:ubuntu /data

# putting some temporary file in the directory
echo "Hello World!, Welcome to a new World" > /data/web_static/releases/test/index.html

string="location /hbnb_static {\n\t\talias \/data\/web_static\/current\/;\n\t}"
sudo sed -i "/listen 80 default_server/a $string" /etc/nginx/sites-enabled/default

sudo service nginx restart
