"""Sparse inverted index used by Vector Ridge."""

from collections import defaultdict


class SparseIndex:
    def __init__(self):
        self.postings = defaultdict(dict)

    def add(self, doc_id, terms):
        for term, weight in terms.items():
            self.postings[term][doc_id] = weight

    def lookup(self, term):
        return self.postings.get(term, {})
