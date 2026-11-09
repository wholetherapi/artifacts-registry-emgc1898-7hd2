"""Ensemble member manager for Mosaic Forecast."""

from statistics import mean


class Ensemble:
    def __init__(self, members):
        self.members = list(members)

    def mean_forecast(self, station):
        values = [member[station] for member in self.members if station in member]
        return mean(values) if values else None

    def spread(self, station):
        values = [member[station] for member in self.members if station in member]
        if not values:
            return 0.0
        return max(values) - min(values)
