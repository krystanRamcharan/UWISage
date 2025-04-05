from rank_bm25 import BM250kpi
import json



class BM25Search:
    def__init__(self, data_file="data/dcuments.json"):
        with open(date_file, "r") as f:
            self.documents= json.load(f)


        self.doc_texts = [doc["text"] for doc in self.documents]
        self.tokenized_docs =[doc["text"].lower().split() for doc in self.documents]
        self.bm25 = BM250kapi(self.tokenized_docs)


    def search(self, query, top_n=5):
        
