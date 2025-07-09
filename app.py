from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import random
import prometheus_client as prom_client

# Uncomment these to show the relevant metrics on /metrics
#prom_client.REGISTRY.unregister(prom_client.PROCESS_COLLECTOR)
#prom_client.REGISTRY.unregister(prom_client.PLATFORM_COLLECTOR)
#prom_client.REGISTRY.unregister(prom_client.GC_COLLECTOR)

app = FastAPI()
metrics_app = prom_client.make_asgi_app()
app.mount("/metrics", metrics_app)

# Define Prometheus metrics
REQUEST_COUNTER = prom_client.Counter(
    "app_requests_total",  # Metric name
    "Total number of requests to the app",  # Metric description
    ["endpoint"],  # Labels (e.g., endpoint name)
)

RANDOM_NUMBER_GAUGE = prom_client.Gauge(
    "app_random_number",  # Metric name
    "Current value of the random number",  # Metric description
)

@app.get("/", response_class=JSONResponse)
def get_homepage():
    # Increment the request counter
    REQUEST_COUNTER.labels(endpoint="/").inc()

    random_number = random.randint(a=0, b=100)

     # Set the random number gauge
    RANDOM_NUMBER_GAUGE.set(random_number)

    return {"status": "ok", "random_number": random_number}