#!/bin/bash

sudo apt update && sudo apt install -y postgresql python3-pip python3-virtualenv default-jre
sudo service postgresql start
wget https://downloads.metabase.com/v0.48.7/metabase.jar