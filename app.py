from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import random
import prometheus_client as prom_client

#
# A dummy app which exposes two pages
# The root: / which is the "app functionality"
# The system metrics at /metrics
# It is the metrics page that the collector will look at
# and periodically retrieve metrics from "ie. scrape"
#
# This app is really a nice-to-have, you could also have just hardcoded
# an HTML page in the correct Prometheus syntax for metrics.
# ie.
#  # HELP app_random_number Current value of the random number
#  # TYPE app_random_number gauge
#  app_random_number 32.0
#

# Uncomment these to show the relevant metrics on /metrics
#prom_client.REGISTRY.unregister(prom_client.PROCESS_COLLECTOR)
#prom_client.REGISTRY.unregister(prom_client.PLATFORM_COLLECTOR)
#prom_client.REGISTRY.unregister(prom_client.GC_COLLECTOR)

app = FastAPI()
# Tell Prometheus to create a sub-application and attach it at /metrics
# It is this sub-application magic that
# translates the Python into a readable Prometheus formatted metrics page
# As mentioned above, you could also hardcode this as a static HTML page
# The collector won't care :)
metrics_app = prom_client.make_asgi_app()
app.mount("/metrics", metrics_app)

# Define Prometheus metrics
# https://prometheus.io/docs/concepts/metric_types/#counter
REQUEST_COUNTER = prom_client.Counter(
    "app_requests_total",  # Metric name
    "Total number of requests to the app",  # Metric description
    ["endpoint"],  # Labels (e.g., endpoint name)
)

# Register a second metric
# https://prometheus.io/docs/concepts/metric_types/#gauge
# A gauge is the most like a "normal" metric
# A guage can have any value at any time
RANDOM_NUMBER_GAUGE = prom_client.Gauge(
    "app_random_number",  # Metric name
    "Current value of the random number",  # Metric description
)

# This is the "real functionality" of the app
# You can probably ignore it. You care about the /metrics endpoint
# Note we don't explicitely define /metrics
# That is handled auto-magically by the make_asgi_app() lines above
@app.get("/", response_class=JSONResponse)
def get_homepage():
    # Increment the request counter
    REQUEST_COUNTER.labels(endpoint="/").inc()

    random_number = random.randint(a=0, b=100)

     # Set the random number gauge
    RANDOM_NUMBER_GAUGE.set(random_number)

    return {"status": "ok", "random_number": random_number}