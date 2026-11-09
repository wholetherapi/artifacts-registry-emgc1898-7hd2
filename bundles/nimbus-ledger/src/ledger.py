"""Minimal settlement engine used by the Nimbus Ledger benchmark."""

from dataclasses import dataclass, field


@dataclass
class Account:
    balance: int = 0
    locked: int = 0


class Ledger:
    def __init__(self):
        self.accounts = {}

    def account(self, name):
        return self.accounts.setdefault(name, Account())

    def settle(self, transfers):
        applied = []
        for src, dst, amount in transfers:
            if self.account(src).balance >= amount:
                self.account(src).balance -= amount
                self.account(dst).balance += amount
                applied.append((src, dst, amount))
        return applied

    def snapshot(self):
        return {name: acct.balance for name, acct in self.accounts.items()}
