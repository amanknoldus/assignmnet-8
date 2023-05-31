Objective >> To Perform Cleaning of Data from a column in blog post data

Input >> csv file

Libraries Used:
    nltk~=3.8.1
    pandas~=2.0.2
    beautifulsoup4~=4.12.2

Steps >>
    Converted csv to dataframe,
    Removed HTML tags From data,
    Removed unwanted thing from data like: symbols, extra spaces, new line tag,
    Performed Tokenization of data to break text into tokens,
    Removed Stopword from data,
    Returned Cleaned Data.

Output >>
    Cleaned Data (Preprocessed Data)
