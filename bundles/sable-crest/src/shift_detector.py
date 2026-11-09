"""Domain-shift detector used by the Sable Crest test suite."""

from statistics import mean, pstdev


def detect(reference, current, z_threshold=2.0):
    mu = mean(reference)
    sigma = pstdev(reference) or 1.0
    z = abs(mean(current) - mu) / sigma
    return {"shifted": z >= z_threshold, "z_score": z}
