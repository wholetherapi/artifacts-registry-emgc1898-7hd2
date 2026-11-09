"""Recall evaluation driver for Vector Ridge."""

from src.index import SparseIndex
from src.retriever import score


def main():
    index = SparseIndex()
    index.add(1, {"sparse": 1.0, "retrieval": 0.7})
    index.add(2, {"learned": 0.9, "index": 0.6})
    print(score({"sparse": 1.0}, index, [1, 2]))


if __name__ == "__main__":
    main()
