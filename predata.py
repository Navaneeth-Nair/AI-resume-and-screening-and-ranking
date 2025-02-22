import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
stopword = set(stopwords.words('english'))
def clean_text():
    text = re.sub(r"\d+", "", text)
    text = re.sub(r"[^\w\s]", "", text)
    words = text.lower().split()
    words = [word for word in words if word not in stopword]
    return " ".join(words)