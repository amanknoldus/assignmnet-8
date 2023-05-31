from src.utils.constants import data_path, stopwords
import pandas as pd
import re
from nltk.tokenize import word_tokenize
from bs4 import BeautifulSoup
import unittest


class TestPreProcessing:

    def __init__(self):
        self.file = data_path

    def test_extract_data(self):
        """
        Function to perform pre_processing operations on data
        @return: preprocessed data
        """
        input_file = self.file
        blog_data = self.test_dataframe_convert(input_file)

        blog_data['Content'] = blog_data['Content'].apply(self.test_remove_html_tags)
        content_data = blog_data['Content']

        filtered_data = self.test_get_filtered_data(content_data)
        tokenized_data = self.get_tokenize_data(filtered_data)
        return tokenized_data

    @staticmethod
    def test_dataframe_convert(input_file):
        """
        Function to convert csv file to dataframe
        @param input_file: csv file
        @return: dataframe
        """
        file_data = pd.read_csv(input_file)
        blog_data = pd.DataFrame(file_data)
        return blog_data

    @staticmethod
    def test_remove_html_tags(text_data):
        """
        Function to remove html tags from data
        @param text_data: series of column: "Content"
        @return: removed html tags data
        """
        soup = BeautifulSoup(text_data, 'html.parser')
        return "Removed HTML Tags"

    @staticmethod
    def test_get_filtered_data(blog_data):
        """
        Function to remove extra spaces, new line tags, symbols
        and convert text to lower case.
        @param blog_data: series of column: "Content"
        @return: textual data after removing unnecessary things
        """
        text_data = re.sub('[^a-zA-Z]', ' ', str(blog_data))
        text_data = re.sub(' +', ' ', text_data)
        text_data = re.sub(r'\b(ha)+\b', '', text_data)
        text_data = text_data.replace('\n', ' ')
        return text_data.lower().strip()

    @staticmethod
    def get_tokenize_data(content_data):
        """
        Function to create tokens of input data
        and remove stopwords from data
        @param content_data: filtered text data
        @return: tokens (text tokens)
        """
        tokens = word_tokenize(content_data)
        tokenized_data = [word for word in tokens if word.lower() not in stopwords]
        return tokenized_data


class TestClass(unittest.TestCase):

    def test_for_dataframe(self):
        """
        Test Function to check for dataframe conversion
        """
        df_check = TestPreProcessing()
        data = df_check.test_dataframe_convert(data_path)
        result = ""
        if isinstance(data, pd.DataFrame):
            result = "This is Dataframe"
        self.assertEqual(result, "This is Dataframe")


if __name__ == '__main__':
    unittest.main()
