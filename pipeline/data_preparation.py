import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

STOPWORDS = set(stopwords.words('english'))

class DataPreparation:
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()

    def tokenize_column(self, text):
        return word_tokenize(text) if isinstance(text, str) else []

    def remove_stopwords(self, tokens):
        return [token for token in tokens if token.lower() not in STOPWORDS]

    def handle_null_values(self, text):
        return text if isinstance(text, str) else ""

    def remove_special_characters(self, text):
        return ''.join(e for e in text if (e.isalnum() or e.isspace()))

    def lemmatize_tokens(self, tokens):
        return [self.lemmatizer.lemmatize(token) for token in tokens]

    def lowercase(self, text):
        return text.lower() if isinstance(text, str) else ""

    def run(self, csv_path, output_path):
        df = pd.read_csv(csv_path)

        for column in ['title', 'description', 'author']:
            df[column] = df[column].apply(self.lowercase).apply(self.handle_null_values)

        df['title_tokens'] = df['title'].apply(self.tokenize_column)
        df['description_tokens'] = df['description'].apply(self.tokenize_column)
        
        df['title_no_stopwords'] = df['title_tokens'].apply(self.remove_stopwords)
        df['description_no_stopwords'] = df['description_tokens'].apply(self.remove_stopwords)
        
        df['title_clean'] = df['title'].apply(self.remove_special_characters)
        df['description_clean'] = df['description'].apply(self.remove_special_characters)
        
        df['title_lemmatized'] = df['title_no_stopwords'].apply(self.lemmatize_tokens)
        df['description_lemmatized'] = df['description_no_stopwords'].apply(self.lemmatize_tokens)
        
        df.drop_duplicates(subset=['title', 'description', 'author'], inplace=True)

        df.to_csv(output_path, index=False)
        
        return output_path