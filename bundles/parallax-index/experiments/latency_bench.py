"""Latency benchmark for Parallax Index."""

import statistics
import time


def run(probe, iterations=1000):
    samples = []
    for _ in range(iterations):
        start = time.perf_counter()
        probe()
        samples.append(time.perf_counter() - start)
    return statistics.median(samples)


if __name__ == "__main__":
    print(run(lambda: sum(range(1000))))
