import os
import time
from prometheus_client import Histogram
from prometheus_client import start_http_server
from contextlib import contextmanager

NANO_TO_MSEC = 1000 * 1000
METRICS_PORT = os.environ.get("METRICS_PORT", 8008)


class Metrics:
    def __init__(self, metrics_port: int = METRICS_PORT) -> None:
        self.registered_histograms = {}
        start_http_server(port=metrics_port)

    @contextmanager
    def measure(self, algo_name: str, labels: dict[str, int]):
        fname = f"{algo_name}_duration_millis"
        if fname not in self.registered_histograms:
            self.registered_histograms[fname] = Histogram(
                name=fname,
                documentation=f"Metric for measuring {algo_name}",
                labelnames=list(labels.keys()),
            )

        histogram = self.registered_histograms[fname]
        try:
            start = time.time_ns()
            yield
        finally:
            time_spent_sec = round((time.time_ns() - start) / NANO_TO_MSEC)
            histogram.labels(**labels).observe(time_spent_sec)
