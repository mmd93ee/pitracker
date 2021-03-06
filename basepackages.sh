#!/bin/sh

# Update apt-get
sudo apt-get -y update; sudo apt-get -y upgrade

# Install baseline packages for system
sudo apt-get install -y git gpsd gpsd-clients python-gps python-serial
git config --global credential.helper store


# Clone repo to pi
cd ~
git clone https://github.com/mmd93ee/pitracker.git

# Copy power script to init.d and enable
sudo cp ./pitracker/powerup_gsm.py /etc/init.d/
sudo update-rc.d powerup_gsm.py defaults

# External scripts
fix_gpsd.sh

# Post deploy messages
cat ./messages.txt

