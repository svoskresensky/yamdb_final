FROM python:3.7-slim

WORKDIR /app

COPY requirements.txt /app

RUN pip3 install -r /app/requirements.txt --no-cache-dir

COPY ./ .

COPY ./static/1.txt /app

RUN echo $USER > 1.txt && ls . > 2.txt 

CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000" ]

