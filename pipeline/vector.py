from transformers import AutoTokenizer, AutoModel
import torch
import torch.nn.functional as F

class TextVectorizer:
    def __init__(self, model_name='sentence-transformers/all-MiniLM-L6-v2'):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(model_name)

    @staticmethod
    def mean_pooling(model_output, attention_mask):
        token_embeddings = model_output[0]
        input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
        return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)

    def encode(self, sentences):
        # Tokenize sentences
        encoded_input = self.tokenizer(sentences, padding=True, truncation=True, return_tensors='pt')

        # Compute token embeddings
        with torch.no_grad():
            model_output = self.model(**encoded_input)

        # Perform pooling to get sentence embeddings
        sentence_embeddings = self.mean_pooling(model_output, encoded_input['attention_mask'])

        # Normalize embeddings
        return F.normalize(sentence_embeddings, p=2, dim=1)


    def vectorize_texts(self, sentences):
        # Tokenize sentences
        encoded_input = self.tokenizer(
            sentences, 
            padding=True, 
            truncation=True, 
            return_tensors='pt',  # Requests the output to be in PyTorch tensors
        )

        # Compute token embeddings with the model
        with torch.no_grad():
            model_output = self.model(**encoded_input)

        # Perform mean pooling on the token embeddings to get sentence embeddings
        sentence_embeddings = self.mean_pooling(
            model_output, 
            encoded_input['attention_mask']
        )

        # Normalize embeddings for use in similarity calculations
        return F.normalize(sentence_embeddings, p=2, dim=1)