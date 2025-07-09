# Metrics AI Repository Development Environment

This repository is a preconfigured development environment with everything you need preinstalled.

You can run this either in a browser (using the free credits GitHub provides) or run it locally (what I recommend).

These instructions assume you're using Visual Studio code, but any IDE should be similar.


1. In VS Code, ensure the `Dev Containers` extension is installed
1. Make sure Docker is running on your machine
1. Clone this code and open it in VS Code
1. Go to `View > Command Palette` and choose `Dev containers: Reopen in Container`
1. Wait for the installation process to complete. When it is done, you'll see `Done. Press any key to close the terminal.`

Congratulations, you are now inside a Docker container and this is your self-contained dev environment.

## Start the App

It is now time to start the Prometheus application.

1. Drop into a Python venv and install the required dependencies

```
source bin/activate
pip install -r requirements.txt
```

Now start the app:

```
fastapi run app.py --host 0.0.0.0 --port 8000
```

## Access the App
The application has two pages:

* `/` - the root path is the "application logic". You're not so interested in this page.
* `/metrics` - this is the page of Prometheus metrics. The collector will "watch" this page

## Start Collector

Finally, let's start the collector to see the metrics being retrieved ("scraped" in Prometheus parlance).

```
./otelcol-contrib --config=collector-config.yaml
```