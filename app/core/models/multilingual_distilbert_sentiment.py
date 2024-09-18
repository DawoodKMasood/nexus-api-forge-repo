from transformers import pipeline

class MultilingualDistilBERTSentiment:
    def __init__(self):
        self.MODEL = "lxyuan/distilbert-base-multilingual-cased-sentiments-student"
        self.classifier = pipeline(
            model=self.MODEL,
            return_all_scores=True
        )

    def predict(self, text):
        results = self.classifier(text)[0]
        return [{"label": result["label"], "score": float(result["score"])} for result in results]

multilingual_distilbert_sentiment = MultilingualDistilBERTSentiment()