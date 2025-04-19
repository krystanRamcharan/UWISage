from bm25_searchengine import BuildIndex

class AIAssistant:

    def __init__(self, documents):
        self.search_engine = BuildIndex(documents)

    def answer_query(self, question):
        parser = QueryParsers('queries.txt')
        query_terms = parser.get_queries_from_string(question)  # We'll tweak the parser
        scores = self.search_engine.BM25scores(query_terms)
        ranked_docs = self.search_engine.ranked_docs_from_scores(scores)
        return ranked_docs

    def create_study_schedule(self, constraints):
        # Your CSP logic goes here
        pass

    def fetch_past_papers(self):
        # Your web scraper logic goes here
        pass

    def fetch_course_outline(self):
        # Your web scraper logic goes here
        pass
