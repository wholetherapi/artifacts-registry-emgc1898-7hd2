"""Batched scorer for the Vector Ridge retrieval experiments."""


def score(query_terms, index, doc_ids):
    scores = {doc: 0.0 for doc in doc_ids}
    for term, weight in query_terms.items():
        for doc, posting_weight in index.lookup(term).items():
            if doc in scores:
                scores[doc] += weight * posting_weight
    return sorted(scores.items(), key=lambda kv: kv[1], reverse=True)
