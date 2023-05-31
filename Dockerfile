FROM python:3.8-slim-buster
WORKDIR /assignment-8
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python3", "main.py"]