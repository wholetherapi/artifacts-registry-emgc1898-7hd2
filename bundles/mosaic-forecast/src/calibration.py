"""Probability calibration routines for Mosaic Forecast."""


def reliability_curve(predicted, observed, bins=10):
    curve = {}
    for lo in range(bins):
        lower = lo / bins
        upper = (lo + 1) / bins
        bucket = [
            (p, o)
            for p, o in zip(predicted, observed)
            if lower <= p < upper or (lo == bins - 1 and p == 1.0)
        ]
        if bucket:
            curve[f"{lower:.2f}-{upper:.2f}"] = (
                sum(p for p, _ in bucket) / len(bucket),
                sum(o for _, o in bucket) / len(bucket),
            )
    return curve
