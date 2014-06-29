# Description
C'est un prjet de site internet de recherche dans une base de données NoSQL MongoDB en python.
Le site est porté par un serveur linux.

#Installation
Le projet fonction très bien sur linux et des librairies sont nécessaires. 
Voici la marche à suivre pour une installation sur ubuntu.

##installation des sources
-cd ~
-git clone https://github.com/tygroo/etronik.git
-sudo apt-get install python-pip

##installation des import necessaires
-sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10
-echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' | sudo tee /etc/apt/sources.list.d/mongodb.list
-sudo apt-get update
-sudo apt-get install mongodb-org
-mkdir /data/db

-sudo apt-get install xsltproc

-sudo pip install jinja2

-sudo pip install cherrypy
-sudo apt-get install python-cherrypy

-sudo pip install pymongo

###Installation de pdfminer
git clone https://github.com/euske/pdfminer.git pdfminer

cd pftminer

sudo python setup.py install
