#!/bin/bash

# Prevent interactive prompt for setting timezone
export DEBIAN_FRONTEND=noninteractive

apt update
apt install -y python3-pip python3 python3.12-venv
python3 -m venv .