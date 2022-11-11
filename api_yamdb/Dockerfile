FROM python:3.7-slim

WORKDIR /app

COPY requirements.txt /app

RUN pip3 install -r /app/requirements.txt --no-cache-dir

COPY ./ .
COPY ./test/2.txt /app
COPY ./static/1.txt /app

RUN echo $USER > a.txt && ls . > b.txt 

CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000" ]

