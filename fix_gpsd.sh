#!/bin/sh

sudo systemctl stop gpsd.socket
sudo systemctl disable gpsd.socket

