import pandas as pd
import os
import json

def load_json(file_path):
    with open(file_path, 'r') as file:
        data = [json.loads(line) for line in file]
        return pd.DataFrame(data)

def load_csv(file_path):
    return pd.read_csv(file_path)

def save_to_json(df, file_path):
    df.to_json(file_path, orient='records', lines=True)
    
def combine_files(json_files, csv_files):
    df_list = []

    total_rows = 0
    max_rows = 10000  # Set the limit for rows

    # Loading and combining data from JSON files
    for file in json_files:
        df = load_json(file)

        if total_rows + len(df) > max_rows:
            df = df.iloc[:max_rows - total_rows]

        total_rows += len(df) 

        df = df.rename(columns={
            'headline': 'title',
            'short_description': 'description',
            'link': 'url',
            'authors': 'author',
            'date': 'publishedAt'
        })
        df['source'] = 'Unknown'  
        df['urlToImage'] = None   
        df['content'] = df['description']  # Set content column to short_description 
        df_list.append(df)

        if total_rows >= max_rows:
            break

    # Loading and combining data from CSV files
    def safe_eval(x):
        try:
            return eval(x)['name']
        except:
            return x

    for file in csv_files:
        df = load_csv(file)
        df['source'] = df['source'].apply(safe_eval)
        df_list.append(df)

    # Concatenate all DataFrames in the list
    combined_df = pd.concat(df_list, ignore_index=True)
    return combined_df

# Define your path
data_directory = '/data'  # replace with your actual path

json_files = [os.path.join(data_directory, f) for f in os.listdir(data_directory) if f.endswith('.json')]
csv_files = [os.path.join(data_directory, f) for f in os.listdir(data_directory) if f.endswith('.csv')]

print(json_files, csv_files)

final_df = combine_files(json_files, csv_files)
print(final_df.head())
print(final_df.shape)
final_df.to_csv('combined_data.csv')
output_json_path = 'combined_data.json'
save_to_json(final_df, output_json_path)
print(f"Data saved to {output_json_path}")
