import pandas as pd
import numpy as np

class DataCleaning:

    def __init__(self):
        pass

    def clean_csv(self, input_path, output_path):
        """
        Load the CSV file, clean it, and save the cleaned data.
        """
        # Load the CSV file into a pandas DataFrame.
        data = pd.read_csv(input_path)

        # Replace infinite values with NaN
        data.replace([np.inf, -np.inf], np.nan, inplace=True)
        
        # List of columns to check for NaN values
        columns_to_check = ["author", "title", "description", "publishedAt", "url"]
        
        # Drop rows with NaN values in the specified columns
        data.dropna(subset=columns_to_check, inplace=True)

        # Save the cleaned data to a CSV file.
        data.to_csv(output_path, index=False)