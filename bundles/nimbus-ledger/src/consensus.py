"""Quorum adapter for the Nimbus Ledger benchmark harness."""

from collections import Counter


class Quorum:
    def __init__(self, members):
        self.members = list(members)
        self.threshold = len(self.members) // 2 + 1

    def commit(self, votes):
        counts = Counter(votes)
        winner, count = counts.most_common(1)[0]
        return winner if count >= self.threshold else None
