from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

class Vectorizer:
    
    def __init__(self):
        self.vectorizer = TfidfVectorizer(stop_words='english', max_features=384)  # Adjust max_features to 384 maybe change this?
    
    def fit(self, corpus):
        self.vectorizer.fit(corpus)
    
    def transform(self, text):
        return self.vectorizer.transform([text])
    
    def fit_transform(self, corpus):
        tfidf_matrix = self.vectorizer.fit_transform(corpus)
        return [vector.toarray()[0] for vector in tfidf_matrix]


    def run(self, csv_path, output_path):
        df = pd.read_csv(csv_path)
        df['text'] = df['title'] + " " + df['description']
        df['vector'] = list(self.fit_transform(df['text']))
        df.to_csv(output_path, index=False)
        return output_path
