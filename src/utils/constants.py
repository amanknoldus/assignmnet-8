from pathlib import Path
from nltk.corpus import stopwords

path = Path(__file__).resolve().parent.parent
dataset_path = path / "dataset"
data_path = dataset_path / "extracted_blog_content.csv"

stopwords = set(stopwords.words('english'))
