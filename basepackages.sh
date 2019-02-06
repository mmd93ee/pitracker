#!/bin/sh

# Update apt-get
sudo apt-get -y update; sudo apt-get -y upgrade

# Install baseline packages for system
sudo apt-get install -y git 

# Clone repo to pi
cd ~
git clone https://github.com/mmd93ee/pitracker.git
cd pitracker
