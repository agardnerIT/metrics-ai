#!/bin/bash

COLLECTOR_VERSION=0.128.0

# Prevent interactive prompt for setting timezone
export DEBIAN_FRONTEND=noninteractive

apt update
apt install -y wget python3-pip python3 python3.12-venv

# Download Collector Binary
wget https://github.com/open-telemetry/opentelemetry-collector-releases/releases/download/v${COLLECTOR_VERSION}/otelcol-contrib_${COLLECTOR_VERSION}_linux_amd64.tar.gz
tar -xvf otelcol-contrib_${COLLECTOR_VERSION}_linux_amd64.tar.gz
# Delete the tar as it has been extracted
# The collector binary is ./otelcol-contrib
rm otelcol-contrib_${COLLECTOR_VERSION}_linux_amd64.tar.gz

# Create Python venv scaffolding
python3 -m venv .