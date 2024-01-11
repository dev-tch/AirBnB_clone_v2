#!/usr/bin/env bash
# Install Nginx if it not already installed
sudo apt-get -y update
sudo apt-get -y install nginx

# create directories 
dir1="/data/web_static/releases/test/"
dir2="/data/web_static/shared/"
link_file="/data/web_static/current"

if [ ! -d "$dir1" ]; then
	sudo mkdir -p "$dir1"
fi
if [ ! -d  "$dir2" ]; then
	sudo mkdir -p "$dir2"
fi

# Create a fake HTML file
html=\
"
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
"
sudo echo  -e  "$html" > "$dir1/index.html"

#  If the symbolic link already exists, it should be deleted
if [ -h "$link_file" ]; then	
	sudo rm /data/web_static/current
fi

# recreate symbolic link 

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current


# Give ownership of the /data/ folder to the ubuntu user AND group 

sudo chown -R ubuntu:ubuntu /data/

# update configuration 

nginx_default_config="/etc/nginx/sites-available/default"
nginx_custom_config="/etc/nginx/sites-available/redirect_config"
if [ -e "$nginx_custom_config" ]; then
	sudo sed -i '/^\s*server_name _;/a\\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}' "$nginx_custom_config"
else
	sudo sed -i '/^\s*server_name _;/a\\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}' "$nginx_default_config"
fi


# reload the server nginx 
if [ "$(pgrep -c nginx)" -le 0 ]; then
  sudo service nginx start
else
  # sudo -S service nginx restart <<< "ubuntu"
  sudo service nginx restart
fi

