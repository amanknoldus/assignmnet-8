from src.preprocessing.preprocessing import PreProcessing


class Pipeline:

    @staticmethod
    def get_data():
        """
        Function to get preprocessed data
        @return: extracted processed data
        """
        process_data = PreProcessing()
        result = process_data.extract_data()
        return result
