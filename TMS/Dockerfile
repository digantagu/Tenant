FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
#RUN pip3 install -r requirements.txt

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2

RUN pip install --upgrade pip

RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "manage.py", "makemigrations"]

CMD [ "python3", "manage.py", "migrate"]

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000"]