# bm25_search.py

import re
from nltk.stem import PorterStemmer

class BuildIndex:
    def __init__(self, docs):
        self.docs = docs  # list of raw text strings
        self.stemmer = PorterStemmer()
        self.doc_texts = [self.preprocess(doc) for doc in self.docs]
        self.index = self.build_index()
        self.doc_lengths = [len(doc) for doc in self.index]
        self.avg_doc_length = sum(self.doc_lengths) / len(self.doc_lengths) if self.doc_lengths else 0
        self.k1 = 1.5
        self.b = 0.75
        self.total_score = {}
        self.rankedDocs = []

    def preprocess(self, text):
        words = re.sub(r'\W+', ' ', text.lower()).split()
        return [self.stemmer.stem(word) for word in words]

    def build_index(self):
        return self.doc_texts

    def BM25scores(self, query):
        scores = {}
        N = len(self.index)
        query_terms = self.preprocess(query)

        for i, doc in enumerate(self.index):
            score = 0
            doc_len = len(doc)
            for term in query_terms:
                f = doc.count(term)
                n_qi = sum(1 for d in self.index if term in d)
                if n_qi == 0:
                    continue
                idf = max(0, (N - n_qi + 0.5) / (n_qi + 0.5))
                numerator = f * (self.k1 + 1)
                denominator = f + self.k1 * (1 - self.b + self.b * doc_len / self.avg_doc_length)
                score += idf * (numerator / denominator)
            scores[f"doc_{i}"] = score
        return scores

    def ranked_docs(self):
        ranked = sorted(self.total_score.items(), key=lambda item: item[1], reverse=True)
        return ranked

    def top_docs(self, query, n=5):
        self.total_score = self.BM25scores(query)
        self.rankedDocs = self.ranked_docs()
        return self.rankedDocs[:n]
