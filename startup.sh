#! /usr/bin/env bash

echo "Ubuntu update running..."
sudo apt-get update

echo "Installing git, curl, python-dev, openjdk-7, make, unzip ..."
sudo apt-get install -y git curl python-dev openjdk-7-jre make unzip vim

echo "Installing python distribute ..."
curl -O http://python-distribute.org/distribute_setup.py
sudo python distribute_setup.py

echo "Installing python pip ..."
curl -O https://raw.github.com/pypa/pip/master/contrib/get-pip.py
sudo python get-pip.py

echo "Installing fabric ..."
sudo pip install fabric

echo "Installing RVM ..."
curl -L https://get.rvm.io | bash -s stable
source /etc/profile.d/rvm.sh
rvm requirements
rvm install 1.9.3
gem install compass

echo "Installing lessc ..."
sudo apt-get install -y node-less

echo "Installing postgress ..."
sudo apt-get install -y postgresql postgresql-contrib python-psycopg2 libpq-dev build-essential

echo "Creating new postgres database ..."
sudo -u postgres createdb hasjob
sudo -u postgres createdb hacknight
sudo -u postgres createdb hgtv
sudo -u postgres createdb imgee
sudo -u postgres createdb peopleflow
sudo -u postgres createdb contactpoint
sudo -u postgres createdb kharcha
sudo -u postgres createdb lastuser

echo "===="
echo "create new postgres user with username hasgeek and password hasgeek"
echo "sudo -u postgres createuser -D -A -P hasgeek"
echo "===="
