
import logging
import sys
import time
import os
from prometheus_client import Histogram
from prometheus_client import start_http_server
from contextlib import contextmanager

NANO_TO_SEC = 1000 * 1000 * 1000

class Metrics:

    def __init__(self, metrics_port: int = 8008) -> None:
        self.registered_histograms = {}
        start_http_server(port=metrics_port)

    @contextmanager
    def measure(self, algo_name: str, labels: dict[str, int]):
        fname = f"{algo_name}_duration_seconds"
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
        except Exception as e:
            raise e
        finally:
            time_spent_sec = round((time.time_ns() - start) / NANO_TO_SEC)
            histogram.labels(list(labels.values())).observe(time_spent_sec)