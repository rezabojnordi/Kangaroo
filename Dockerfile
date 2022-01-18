FROM python:3.8.12

RUN mkdir /app

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir  -r requirements.txt --quiet

EXPOSE 5000

CMD ["python", "./src/main.py"]

