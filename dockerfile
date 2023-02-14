FROM python:3.10.5

WORKDIR /todo-api

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY .env .env

COPY ./api ./api

COPY app.py app.py

CMD ["sh", "-c", "python app.py"]

