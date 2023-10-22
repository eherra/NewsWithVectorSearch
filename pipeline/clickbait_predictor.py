# classify.py
import torch
import pandas as pd
from pipeline.model.train import ClickbaitClassifier 
from pipeline.vector import TextVectorizer
class ClickbaitPredictor:
    def __init__(self, model_path="pipeline/model/models/clickbait_classifier.pth", vectorizer='sentence-transformers/all-MiniLM-L6-v2'):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.vectorizer = TextVectorizer()
        self.model = self.load_model(model_path).to(self.device)
        

    def load_model(self, model_path):
        """
        Load the trained model from the specified path.
        """
        model = ClickbaitClassifier(input_dim=384)  # or whatever your input dimension is
        model.load_state_dict(torch.load(model_path, map_location=self.device))
        return model

    def predict(self, titles):
        if not isinstance(titles, pd.Series):
            raise TypeError("Input must be a Pandas Series")
        titles_list = titles.tolist()
     

        inputs = self.vectorizer.vectorize_texts(titles_list)
        inputs = inputs.to(self.device)
        self.model.eval()
        # Prediction part remains unchanged
        with torch.no_grad():
            outputs = self.model(inputs)
            preds = torch.round(outputs).int().cpu().numpy()
        return preds.tolist()


