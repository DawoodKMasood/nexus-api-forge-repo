from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
import torch

class DistilBERTSST2:
    def __init__(self):
        self.tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
        self.model = DistilBertForSequenceClassification.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")

    def predict(self, text):
        inputs = self.tokenizer(text, return_tensors="pt")
        with torch.no_grad():
            logits = self.model(**inputs).logits

        predicted_class_id = logits.argmax().item()
        return self.model.config.id2label[predicted_class_id]

distilbert_sst2 = DistilBERTSST2()