from src.pipeline.pipeline import Pipeline

if __name__ == '__main__':
    res = Pipeline()
    response = res.get_data()
    print("Pre-Processed-Data: ", response)
