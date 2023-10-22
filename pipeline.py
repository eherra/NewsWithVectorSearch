import pandas as pd
import os
# pipeline.data_preparation import DataPreparation
from pipeline.ingest import Ingest
from pipeline.data_extraction import DataExtraction
from pipeline.data_preparation import DataPreparation
from pipeline.data_cleaning import DataCleaning  
from pipeline.clickbait_predictor import ClickbaitPredictor

from dotenv import load_dotenv
load_dotenv()



class Pipeline:
    def __init__(self):
        self.dp = DataPreparation()
        self.ingest = Ingest()
        self.extractor = DataExtraction()
        self.cleaner = DataCleaning()
        self.predictor = ClickbaitPredictor()


    def run(self):
        
        # Step 0: Data Extraction
        extracted_path = self.extractor.run("extracted_data.csv")

        # Step 0.5: Data Cleaning
        cleaned_path = "cleaned_data.csv"
        self.cleaner.clean_csv(extracted_path, cleaned_path)

        # Step 1: Data Preparation
        processed_data_path = self.dp.run(cleaned_path, output_path="path_for_processed_data.csv")
        
        # Read and process data
        df = pd.read_csv("/home/richard/Documents/lipasto/NewsWithVectorSearch/path_for_processed_data.csv")


        # Step 2: Clickbait Prediction
        titles_no_stopwords = df['title_clean']
        predictions = self.predictor.predict(titles_no_stopwords)
        df['is_clickbait'] = predictions

        # Filter out the clickbait articles based on predictions (1: clickbait, 0: not clickbait)
        df['is_clickbait'] = df['is_clickbait'].apply(lambda x: x[0])
        filtered_df = df[df['is_clickbait'] == 0]

        # Step 3: Ingestion and vectorize
        self.ingest.run(filtered_df)


if __name__ == "__main__":
    pipeline = Pipeline()
    pipeline.run()