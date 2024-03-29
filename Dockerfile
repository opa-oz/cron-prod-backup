FROM python:3.9-slim
LABEL authors="opa-oz"

WORKDIR /code

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY main.py /code/main.py

CMD ["python", "main.py"]