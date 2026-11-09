"""Rolling-origin backtest driver for Mosaic Forecast."""

from src.calibration import reliability_curve


def main():
    predicted = [0.1, 0.35, 0.6, 0.85, 0.95]
    observed = [0, 0, 1, 1, 1]
    print(reliability_curve(predicted, observed))


if __name__ == "__main__":
    main()
