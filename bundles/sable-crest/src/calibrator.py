"""Shift-aware calibrator for Sable Crest."""


class ShiftCalibrator:
    def __init__(self, temperature=1.0):
        self.temperature = temperature

    def calibrate(self, logits):
        scaled = [value / self.temperature for value in logits]
        total = sum(2.718281828 ** value for value in scaled)
        return [2.718281828 ** value / total for value in scaled]
