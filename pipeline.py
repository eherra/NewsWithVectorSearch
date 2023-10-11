import pandas as pd
import os
# pipeline.data_preparation import DataPreparation
from pipeline.ingest import Ingest
from pipeline.data_extraction import DataExtraction
from pipeline.data_preparation import DataPreparation
from pipeline.data_cleaning import DataCleaning  

from dotenv import load_dotenv
load_dotenv()



class Pipeline:
    def __init__(self):
        self.dp = DataPreparation()
        self.ingest = Ingest()
        self.extractor = DataExtraction()
        self.cleaner = DataCleaning()

    def run(self):
        # Step 0: Data Extraction
        extracted_path = self.extractor.run("extracted_data.csv")

        # Step 0.5: Data Cleaning
        cleaned_path = "cleaned_data.csv"
        self.cleaner.clean_csv(extracted_path, cleaned_path)

        # Step 1: Data Preparation
        processed_data_path = self.dp.run(cleaned_path, output_path="path_for_processed_data.csv")

        # Read and process data
        df = pd.read_csv(processed_data_path)

        # Step 3: Ingestion and vectorize
        self.ingest.run(df)


if __name__ == "__main__":
    pipeline = Pipeline()
    pipeline.run()