from transformers import AutoTokenizer, AutoModel
import torch

MODEL_NAME = "distilbert-base-uncased"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

model = AutoModel.from_pretrained(MODEL_NAME)

def generate_embedding(text):

    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True
    )

    with torch.no_grad():

        outputs = model(**inputs)

    embedding = outputs.last_hidden_state.mean(dim=1)

    return embedding.squeeze().numpy()