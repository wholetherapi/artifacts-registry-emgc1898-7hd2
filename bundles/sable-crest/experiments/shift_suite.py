"""Evaluation driver for the Sable Crest domain-shift suite."""

from src.calibrator import ShiftCalibrator
from src.shift_detector import detect


def main():
    reference = [0.1, 0.2, 0.15, 0.3]
    current = [0.4, 0.5, 0.45, 0.6]
    print(detect(reference, current))
    print(ShiftCalibrator(1.5).calibrate([1.0, 2.0, 0.5]))


if __name__ == "__main__":
    main()
