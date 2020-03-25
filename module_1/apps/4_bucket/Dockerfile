FROM python:3

ADD bucket.py /

RUN pip install prometheus_client

EXPOSE 8001
EXPOSE 8000

CMD [ "python3", "./bucket.py" ]
