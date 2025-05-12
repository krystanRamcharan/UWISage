import nltk.stem
from uwilinc_search import fetch_uwilinc_results
from bm25_search import BuildIndex
from nltk.stem import PorterStemmer
import re

def preprocess_query(query):
    stemmer = PorterStemmer()
    query = re.sub(r'\W+', ' ', query.lower()).split()
    return [stemmer.stem(word) for word in query]

def main():
    query = input("Enter your UWIlinC search query: ")
    docs = fetch_uwilinc_results(query)
    print(docs)

    if not docs:
        print("No documents found.")
        return

    processed_query = preprocess_query(query)
    bm = BuildIndex(docs)
    results = bm.top_docs(query)

    print("\nTop Search Results:\n")
    for i, (doc_id, score) in enumerate(results, 1):
        print(f"{i}. {doc_id} - Score: {score:.4f}")
        print(f"Content: {docs[int(doc_id.split('_')[-1])][:300]}...\n")
        

if __name__ == "__main__":
    main()
