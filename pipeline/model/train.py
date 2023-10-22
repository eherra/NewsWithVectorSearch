import os
import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report
from pipeline.vector import TextVectorizer

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

import os
from dotenv import load_dotenv
load_dotenv()
DATA_PATH = os.getenv('PATH_TO_TRAINING_DATA')


# Load stopwords
stop_words = set(stopwords.words('english'))
def preprocess_text(text):
    words = word_tokenize(text)
    words = [word.lower() for word in words]
    words = [word for word in words if word.isalnum()]
    filtered_words = [word for word in words if word not in stop_words]
    return " ".join(filtered_words)



def prepare_data(data_path):
    # Load and preprocess data
    data = pd.read_csv(data_path)
    data['headline'] = data['headline'].apply(preprocess_text)

    # Splitting and vectorizing data
    train_texts, test_texts, train_labels, test_labels = train_test_split(
        data['headline'], data['clickbait'], test_size=0.2, random_state=42
    )

    train_texts_list = train_texts.tolist()
    test_texts_list = test_texts.tolist()

    vectorizer = TextVectorizer(model_name='sentence-transformers/all-MiniLM-L6-v2')
    X_train = vectorizer.encode(train_texts_list)
    X_test = vectorizer.encode(test_texts_list)

    # Convert labels to Tensors
    y_train = torch.tensor(train_labels.values).float()
    y_test = torch.tensor(test_labels.values).float()

    return X_train, X_test, y_train, y_test




class ClickbaitDataset(Dataset):
    def __init__(self, features, labels):
        self.features = features
        self.labels = labels

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        return self.features[idx], self.labels[idx]




class ClickbaitClassifier(nn.Module):
    def __init__(self, input_dim):
        super(ClickbaitClassifier, self).__init__()
        self.fc = nn.Linear(input_dim, 1)

    def forward(self, x):
        x = self.fc(x)
        return torch.sigmoid(x)



# Training process
def train_model(model, criterion, optimizer, train_loader, epochs=5):
    model.train()
    for epoch in range(epochs):
        for batch in train_loader:
            optimizer.zero_grad()
            inputs, labels = batch
            outputs = model(inputs).squeeze()
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
        print(f"Epoch: {epoch+1}, Loss: {loss.item()}")

    print("Finished Training")

def evaluate_model(model, X_test, y_test):
    model.eval()
    with torch.no_grad():
        predictions = model(X_test).squeeze()
        predictions = (predictions > 0.5).int()  # Setting a threshold
        report = classification_report(y_test, predictions)
    return report


def save_model(model, save_directory, model_filename):
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    model_save_path = os.path.join(save_directory, model_filename)

    torch.save(model.state_dict(), model_save_path)
    print(f"Model state dictionary saved at {model_save_path}")


def main():
    DATA_PATH = os.getenv('PATH_TO_TRAINING_DATA')
    
    # Prepare data
    X_train, X_test, y_train, y_test = prepare_data(DATA_PATH)

    # Dataset instances
    train_dataset = ClickbaitDataset(X_train, y_train)
    train_loader = DataLoader(train_dataset, batch_size=16, shuffle=True)

    # Model preparation
    input_dim = X_train.shape[1]
    model = ClickbaitClassifier(input_dim)

    # Loss and optimizer
    criterion = nn.BCELoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    # Training the model
    train_model(model, criterion, optimizer, train_loader)

    # Evaluate the model
    report = evaluate_model(model, X_test, y_test)
    print(report)
    
    save_directory = os.getenv('PATH_TO_MODELS')
    model_filename = "clickbait_classifier.pth"

    # Call the function to save the model
    save_model(model, save_directory, model_filename)

if __name__ == "__main__":
    main()
