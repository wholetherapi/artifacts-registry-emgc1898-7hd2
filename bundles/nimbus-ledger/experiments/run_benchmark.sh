#!/usr/bin/env bash
set -euo pipefail
python -m src.ledger --fixture data/fixture_orders.csv --replicas 5
